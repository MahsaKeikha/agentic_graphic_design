from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("brief", "concept", "layout", "accessibility", "review"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_support_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_package_can_release():
    assert authorize("release_support_package", approved_context())["allowed"] is True


def test_asset_license_gap_blocks():
    assert authorize("release_support_package", approved_context() | {"asset_license_gap": True})["allowed"] is False


def test_accessibility_failure_blocks():
    assert authorize("release_support_package", approved_context() | {"accessibility_failure": True})["allowed"] is False


def test_brand_misrepresentation_blocks():
    assert authorize("release_support_package", approved_context() | {"brand_misrepresentation": True})["allowed"] is False


def test_deceptive_design_risk_blocks():
    assert authorize("release_support_package", approved_context() | {"deceptive_design_risk": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
