"""Held-out governance scenarios for F134."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"copyright_similarity_risk": True}, False),
    (base() | {"asset_license_gap": True}, False),
    (base() | {"accessibility_failure": True}, False),
    (base() | {"brand_misrepresentation": True}, False),
    (base() | {"privacy_likeness_risk": True}, False),
    (base() | {"deceptive_design_risk": True}, False),
    (base() | {"production_quality_gap": True}, False),
    (base() | {"content_provenance_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F134 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
