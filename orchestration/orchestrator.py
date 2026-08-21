from AGENTS import brief_agent,concept_agent,layout_agent,accessibility_agent,review_agent
def run(c): return {'brief':brief_agent.run(c),'concept':concept_agent.run(c),'layout':layout_agent.run(c),'accessibility':accessibility_agent.run(c),'review':review_agent.run(c)}
