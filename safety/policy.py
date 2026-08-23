"""Fail-closed governance for F134 Agentic Graphic Design."""

PROTECTED_ACTIONS = {
    "publish_design",
    "send_to_print",
    "approve_asset_license",
    "approve_final_brand_use",
    "deploy_public_creative",
    "external_distribution",
}

REQUIRED_REVIEWS = (
    "brief_reviewed",
    "concept_reviewed",
    "layout_reviewed",
    "accessibility_reviewed",
    "rights_provenance_reviewed",
    "brand_content_reviewed",
    "quality_reviewed",
    "qualified_design_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding design, publication, or licensing action is outside reference-system scope"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required graphic-design review", "missing": missing}
    checks = {
        "copyright_similarity_risk": "copyright, plagiarism, or excessive similarity risk unresolved",
        "asset_license_gap": "asset license, font, image, illustration, or source provenance unresolved",
        "accessibility_failure": "material accessibility or legibility requirement unresolved",
        "brand_misrepresentation": "brand identity, endorsement, affiliation, or trademark use is misleading or unresolved",
        "privacy_likeness_risk": "privacy, likeness, consent, or real-person imagery risk unresolved",
        "deceptive_design_risk": "deceptive, manipulative, or materially misleading design risk unresolved",
        "production_quality_gap": "required output, preflight, or production quality is incomplete",
        "content_provenance_gap": "material content or source provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "graphic-design governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "graphic-design support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
