# KYC Banking API — DevOps Pipeline Reference

> **Demo only.** This repository is an illustrative learning example. It is **not production-certified**, has not been assessed against banking, privacy, security, or regulatory requirements, and must not be used to process real customer information or make identity-verification decisions.
>
> Never commit real customer PII, credentials, tokens, certificates, production data, or live banking/KYC integrations. All API responses and data in this example are synthetic.

A small Python API scaffold and GitHub Actions pipeline showing a typical delivery path:

1. Python style and static security checks
2. Unit tests and dependency vulnerability audit
3. Container build and Trivy image scan
4. Manual, environment-gated deployment placeholder

## Repository layout

```text
.github/workflows/ci-cd.yml  CI, image build/scan, manual deployment gate
src/kyc_api/                 Synthetic KYC status API scaffold
tests/                       Unit tests; no live integrations
Dockerfile                   Non-root, minimal Python image
requirements*.txt            Runtime and development dependencies
k8s/                         Illustrative Kubernetes manifests
```

## Run locally

Requires Python 3.12+ and Docker.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
PYTHONPATH=src pytest -q
uvicorn kyc_api.main:app --reload
```

The demo endpoint is `GET /health` and `POST /v1/kyc/check`. The request accepts a synthetic `application_id` and `country_code`; the response is a fixed illustrative status. It does not collect documents, validate identity, persist data, or contact a bank.

Build locally:

```bash
docker build -t kyc-api:local .
docker run --rm -p 8000:8000 kyc-api:local
```

## CI/CD behavior

On pull requests and pushes to `main`, GitHub Actions runs Ruff lint/format checks, Bandit, pytest, and `pip-audit`. It then builds the image and scans it with Trivy. The workflow uses least-privilege `GITHUB_TOKEN` permissions and does not publish the image by default.

A deployment placeholder can be started manually with **Actions → KYC CI/CD → Run workflow**. Its job targets the GitHub `production` environment, which allows repository owners to configure required reviewers and deployment branch restrictions. The placeholder intentionally performs no cluster connection or rollout. Replace it only with an organization-approved deployment process and short-lived credentials (for example, OIDC); never add credentials to this repository.

To enable GitHub environment protections:

1. Open **Settings → Environments → production**.
2. Add required reviewers and restrict deployment branches/tags to approved refs.
3. Protect `main` with required pull request reviews and successful status checks.
4. Keep Actions permissions read-only by default and review every permission change.

Environment protection rules depend on the GitHub plan and repository visibility. Configure them in GitHub; workflow YAML alone cannot enforce reviewer approvals.

## Kubernetes example

`k8s/` contains a namespace, non-root deployment, resource limits, health probes, and a ClusterIP service. The deployment references a placeholder image and intentionally omits ingress, secrets, customer data, and a real cluster target. Review and adapt every setting with your platform/security teams before use. The workflow does not apply these manifests.

## Safety and production limits

This is a **reference/demo only**, not production-certified. It omits real KYC, AML, sanctions screening, data retention, audit evidence, encryption/key management, threat modeling, operational controls, resilience, regulatory mapping, and independent security validation. Do not connect it to a live banking system or use it for real identity decisions. Use fabricated test data only.

## License

MIT (see `LICENSE`). Third-party actions and packages remain subject to their own licenses.
