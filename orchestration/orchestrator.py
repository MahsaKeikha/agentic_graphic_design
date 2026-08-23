from AGENTS import accessibility_agent, brief_agent, concept_agent, layout_agent, review_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "brief": brief_agent.run(case),
        "concept": concept_agent.run(case),
        "layout": layout_agent.run(case),
        "accessibility": accessibility_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
