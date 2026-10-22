"""Illustrative KYC status API. No real identity checks or integrations."""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="KYC Demo API", version="0.1.0")


class KycCheckRequest(BaseModel):
    """Synthetic input. Never send real customer data to this demo."""

    application_id: str = Field(min_length=1, max_length=32, pattern=r"^[A-Z0-9-]+$")
    country_code: str = Field(min_length=2, max_length=2, pattern=r"^[A-Z]{2}$")


class KycCheckResponse(BaseModel):
    application_id: str
    status: Literal["review_required"]
    message: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/kyc/check", response_model=KycCheckResponse)
def check_kyc(request: KycCheckRequest) -> KycCheckResponse:
    """Return a fixed demo result; no documents or identity are evaluated."""
    return KycCheckResponse(
        application_id=request.application_id,
        status="review_required",
        message="Synthetic demo response; no identity verification was performed.",
    )
