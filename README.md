# F134 | Agentic Graphic Design | L3 Gold Standard | v1.0

A governed five-agent reference architecture for graphic-design decision support across brief interpretation, visual concept development, layout systems, typography, color, imagery, accessibility, rights provenance, brand integrity, production quality, and qualified human design approval.

F134 can organize design requirements, develop original visual directions, reason about hierarchy and layout, check accessibility constraints, track asset provenance, and prepare review packages. It cannot autonomously publish designs, send files to print, approve licenses, authorize final brand use, deploy public creative, or distribute assets externally.

## Graphic-design lifecycle

```text
Brief and Constraints
        -> Concept Development
        -> Visual System and Layout
        -> Accessibility and Content Review
        -> Rights, Brand, Provenance, and Production Review
        -> Qualified Human Design Approval
        -> Human-Controlled Publication or Production
```

The workflow fails closed when required reviews are missing or when material copyright, licensing, accessibility, brand, privacy, deceptive-design, production-quality, or provenance risks remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Brief Agent | Interprets objective, audience, deliverables, channels, constraints, content, and success criteria | What problem must the design solve? |
| Concept Agent | Develops original visual territories, metaphors, mood, art direction, and rationale | What visual idea best expresses the brief? |
| Layout Agent | Organizes hierarchy, grid, typography, imagery, spacing, composition, and responsive variants | Does the visual system communicate clearly and consistently? |
| Accessibility Agent | Reviews contrast, legibility, information redundancy, reading order, text alternatives, and inclusive presentation | Can the intended audience perceive and understand the design? |
| Review Agent | Integrates quality, rights, provenance, brand, content, privacy, production, and approval state | Is the design package appropriate for qualified human use? |

Agents support designers and creative teams. They do not replace art directors, graphic designers, illustrators, photographers, accessibility specialists, brand owners, printers, legal counsel, rights professionals, production vendors, or accountable approvers.

## Repository structure

```text
AGENTS/
├── brief_agent.py
├── concept_agent.py
├── layout_agent.py
├── accessibility_agent.py
└── review_agent.py

SKILLS/
├── brief_reasoning.py
├── concept_reasoning.py
├── layout_reasoning.py
├── accessibility_reasoning.py
└── review_reasoning.py

TOOLS/
├── brief_parser.py
├── concept_board.py
├── layout_grid.py
├── accessibility_check.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Brief architecture

The policy requires `brief_reviewed`. A design brief should preserve objective, audience, message, required content, deliverables, channels, dimensions, deadlines, brand constraints, accessibility requirements, production method, rights constraints, and approval owners.

Ambiguous briefs should expose assumptions instead of silently inventing business requirements.

## Audience and context

Design decisions depend on where, how, and by whom material will be encountered. A billboard, medication instruction, annual report, mobile ad, event poster, packaging label, slide, social graphic, and accessibility notice have different viewing conditions and information priorities.

## Deliverables

Each deliverable should define format, dimensions, orientation, resolution, color space, bleed where applicable, file type, platform constraints, localization needs, accessibility requirements, and production owner.

## Concept development

The policy requires `concept_reviewed`. The Concept Agent can explore visual metaphors, composition strategies, art direction, image treatment, typography direction, graphic motifs, and alternate territories.

Concepts should be tied to the brief rather than generated as decoration without communicative purpose.

## Originality

F134 should create original visual expression and avoid reproducing protected artwork, logos, layouts, illustrations, or other distinctive expression from existing works.

`copyright_similarity_risk` blocks release when copyright, plagiarism, or excessive similarity concerns remain unresolved.

## References and mood boards

References can communicate tone, period, material, composition, photography, or visual vocabulary. They should guide high-level direction rather than become instructions to duplicate a protected work or living creator's distinctive style.

## Visual hierarchy

Hierarchy directs attention through scale, position, contrast, spacing, grouping, typography, imagery, sequence, and repetition. Important information should not depend on arbitrary decoration or hidden assumptions about reading behavior.

## Layout systems

The policy requires `layout_reviewed`. `TOOLS/layout_grid.py` provides a deterministic surface for layout reasoning. Grids can define margins, columns, gutters, modules, baselines, alignment, responsive behavior, and safe areas.

A grid supports consistency but should not override communication needs.

## Composition

Composition can balance focal points, negative space, rhythm, tension, symmetry, asymmetry, scale, direction, and visual weight. F134 can identify crowded or ambiguous compositions while leaving aesthetic judgment to qualified humans.

## Typography

Typography should account for typeface role, hierarchy, size, weight, line length, leading, tracking, alignment, case, numerals, punctuation, language coverage, licensing, and rendering environment.

Font choice is both a creative and rights decision.

## Font licensing

`asset_license_gap` blocks release when font licensing or permitted use is unresolved. Desktop, web, app, broadcast, server, embedding, template, and commercial distribution licenses can differ.

F134 must not represent a font as licensed merely because a file is technically available.

## Color systems

Color can communicate hierarchy, state, brand, emotion, categorization, and emphasis. Production implementations should preserve color definitions appropriate to the medium, such as RGB, CMYK, spot colors, or organization-defined tokens.

Color should not be the only carrier of essential information when accessibility requires redundancy.

## Contrast

The policy requires `accessibility_reviewed`. `accessibility_failure` blocks release when material contrast, legibility, reading-order, or other accessibility requirements remain unresolved.

Contrast should be evaluated in the actual intended context, including text size, weight, background imagery, overlays, states, and environmental viewing conditions.

## Legibility

Legibility depends on type size, typeface, spacing, line length, contrast, language, display quality, motion, viewing distance, and audience needs. A visually elegant design that cannot be read fails its communication purpose.

## Information accessibility

Essential meaning should not rely solely on color, subtle visual distinction, decorative typography, or inaccessible imagery. Alternative formats or text equivalents may be required depending on medium.

## Reading order

Documents, presentations, digital graphics, and exported assets can require logical reading order for assistive technology. Visual placement alone does not guarantee accessible structure.

## Alternative text

Informative images used in digital contexts may require concise text alternatives. Decorative imagery can be treated differently. Alt text should communicate purpose rather than mechanically list pixels.

## Inclusive design

Inclusive design considers disability, age, language, literacy, device access, cultural context, viewing conditions, and cognitive load without assuming a single average user.

## Imagery

Images can include photography, illustration, diagrams, icons, textures, generated imagery, screenshots, archival assets, or licensed stock. Every material asset should have traceable provenance and permitted use.

## Asset provenance

The policy requires `rights_provenance_reviewed`. Asset records can preserve source, creator, license, purchase or permission evidence, restrictions, modification rights, expiration, attribution requirements, model releases, property releases, and project use.

`content_provenance_gap` blocks release when material source provenance is incomplete.

## Stock assets

Stock licensing can restrict print runs, merchandise, resale, templates, sensitive uses, logo use, or large-scale distribution. F134 should preserve license conditions rather than assuming all stock is unrestricted.

## Photography

Photography review can include crop, resolution, consent, model release, property release, manipulation, caption accuracy, context, privacy, and rights.

## Real-person imagery

`privacy_likeness_risk` blocks release when consent, privacy, likeness, publicity, or model-release concerns remain unresolved.

Public availability of an image is not equivalent to permission for every commercial or promotional use.

## Generated imagery

AI-generated or synthetic imagery should be labeled or documented where organizational policy, platform rules, contractual requirements, or context require it. Teams should preserve generation provenance and avoid misleading claims about real events or people.

## Image manipulation

Retouching, compositing, removal, insertion, and generative editing can be legitimate creative tools. Materially deceptive manipulation is inappropriate when the design is presented as factual evidence or authentic documentation.

## Illustration

Illustration can communicate abstraction, narrative, instruction, or brand personality. Commissioned and licensed illustration should preserve creator rights, scope, attribution, exclusivity, and modification terms.

## Icons

Icons should be understandable in context and accompanied by labels when ambiguity is consequential. Icon libraries can have licensing and attribution requirements.

## Logos

Logo creation should consider distinctiveness, reproduction, small-size behavior, monochrome use, spacing, variants, and potential trademark conflicts. F134 does not perform legal trademark clearance.

## Trademark and brand marks

Third-party marks should not imply sponsorship, partnership, certification, or endorsement without authorization.

`brand_misrepresentation` blocks release when brand identity, affiliation, endorsement, or trademark use is materially misleading or unresolved.

## Brand systems

The policy requires `brand_content_reviewed`. Brand review can include approved marks, typography, color, imagery, voice, composition, naming, legal lines, co-branding, and channel-specific rules.

## Brand evolution

A design system can evolve. F134 should distinguish current approved standards from legacy assets and experimental proposals.

## Co-branding

Co-branded materials can require rules for logo order, size, clear space, naming, legal attribution, and approval from multiple organizations.

## Content integrity

Graphic design frequently contains claims, statistics, dates, prices, quotes, instructions, disclaimers, addresses, contact details, or calls to action. Visual polish does not verify factual accuracy.

Content requiring factual, legal, medical, financial, scientific, or regulatory review should be escalated to qualified owners.

## Data visualization

Charts and infographics should preserve scale, denominator, units, time window, source, uncertainty, and visual proportionality. Decorative distortion should not create a false impression of magnitude or trend.

## Misleading graphics

`deceptive_design_risk` blocks release when layout, scale, hierarchy, imagery, interface-like elements, disclaimers, or visual framing materially mislead the audience.

## Dark patterns

Graphic design should not intentionally obscure material information, simulate false urgency, hide costs, disguise advertisements, make cancellation information unreadable, or visually coerce users into choices they would not otherwise make.

## Disclosures

Required disclosures should be readable and appropriately proximate to the claim or action they qualify. F134 should not treat technically present but functionally unreadable text as adequate communication.

## Editorial design

Editorial work can include covers, spreads, reports, magazines, books, white papers, and long-form documents. Systems should preserve hierarchy, running elements, pagination, captions, references, tables, and accessibility across pages.

## Posters

Poster design should account for viewing distance, primary message, environmental clutter, hierarchy, call to action, accessibility, and reproduction conditions.

## Social media graphics

Social assets should preserve platform dimensions, safe areas, mobile legibility, caption relationship, localization, rights, and campaign versioning. F134 does not autonomously publish to social platforms.

## Advertising creative

Advertising designs can require substantiation, disclosures, platform policy review, audience appropriateness, rights, and brand approval. The system should not fabricate testimonials, endorsements, awards, prices, or performance claims.

## Packaging

Packaging design can involve dielines, barcodes, ingredients, warnings, regulatory copy, accessibility, material constraints, printing, finishes, and jurisdiction-specific requirements. Qualified regulatory and production review remains necessary.

## Labels and instructions

Safety-critical labels and instructions require domain-specific review. Visual design can support comprehension but cannot independently determine required warnings or regulatory language.

## Wayfinding and signage

Signage design can involve visibility, distance, lighting, multilingual needs, pictograms, accessibility, building codes, emergency use, and physical installation constraints.

## Environmental graphics

Environmental work should account for architecture, scale, materials, fabrication, mounting, viewing angles, lighting, durability, accessibility, and site permissions.

## Presentation design

Presentation systems can organize hierarchy, templates, diagrams, charts, image treatment, speaker support, and accessibility. Slides should support rather than replace the presenter's argument.

## Infographics

Infographics should separate sourced facts from interpretation and illustration. Icons or area graphics should not imply numerical relationships that the data does not support.

## Print production

`send_to_print` is protected. Print readiness can include trim, bleed, safe area, color space, image resolution, overprint, transparency, spot colors, fonts, dielines, page count, binding, paper, finishing, and printer specifications.

## Preflight

`production_quality_gap` blocks release when required output checks are incomplete. Preflight should be appropriate to the production channel rather than a generic checklist.

## Bleed and trim

Elements intended to reach the edge of a printed piece generally require appropriate bleed according to vendor specifications. Critical content should remain inside safe areas.

## Resolution

Raster image requirements depend on physical size, viewing distance, output device, and production process. Enlarging a low-resolution asset does not restore missing detail.

## Color management

Screen appearance is not a guarantee of printed appearance. Production workflows can require profiles, proofing, spot-color definitions, substrate testing, or printer-specific settings.

## Proofing

Soft proofs, digital proofs, contract proofs, prototypes, and press checks serve different purposes. Final production approval remains human-controlled.

## Digital export

Digital outputs can require pixel dimensions, file-size limits, transparency, compression, responsive variants, accessibility metadata, and platform-specific formats.

## Responsive design assets

Campaign systems may need multiple aspect ratios and crops. Important content should remain valid across variants rather than simply being mechanically resized.

## Localization

Translated text can expand, contract, change reading direction, require different fonts, alter line breaks, or carry different cultural implications. Layout should be tested with actual localized content.

## Right-to-left languages

RTL layouts can require mirrored flow, correct punctuation behavior, compatible typefaces, bidirectional text handling, and culturally appropriate composition. Mirroring every visual element is not automatically correct.

## Multilingual typography

Typeface systems should support required scripts, diacritics, numerals, punctuation, shaping, and weights. Visual consistency should not come at the cost of incorrect language rendering.

## Cultural context

Symbols, colors, gestures, clothing, maps, flags, religious imagery, and historical references can carry different meanings across communities. Qualified cultural review may be appropriate.

## Maps

Maps can involve disputed boundaries, political labeling, scale, projection, data source, accessibility, and legal requirements. F134 should not silently resolve contested geographic representations.

## Sensitive imagery

Graphic material involving violence, illness, disaster, children, grief, sexuality, or vulnerable people should be reviewed for consent, dignity, context, audience, and legitimate purpose.

## Children

Images and personal information involving minors require heightened privacy, consent, safeguarding, and distribution controls.

## Accessibility testing

`TOOLS/accessibility_check.py` provides a deterministic surface for accessibility review. Production implementations can integrate contrast checks, document tagging validation, reading-order checks, text-size thresholds, and other channel-appropriate tests.

Automated checks do not replace human accessibility review.

## Quality review

The policy requires `quality_reviewed`. Quality includes accuracy, consistency, alignment, spacing, typography, imagery, asset integrity, accessibility, export correctness, production requirements, and absence of unintended artifacts.

## Pixel-level defects

Unexpected clipping, masks, transparency seams, missing fonts, broken links, compression artifacts, rasterization, incorrect crops, and export substitutions can appear only in final outputs. Review should include the actual deliverable, not only the source file.

## Content overflow

Localization, dynamic content, template use, or late copy changes can create overflow. Production workflows should test worst-case content where practical.

## Templates

Templates should distinguish editable content, locked brand elements, safe zones, accessibility constraints, and export requirements. A template should reduce inconsistency without preventing legitimate adaptation.

## Design systems

Graphic systems can define tokens, typography, spacing, grids, iconography, image treatments, templates, and reusable components. Versioning should identify which system state produced each deliverable.

## File naming

Consistent names can encode project, deliverable, channel, locale, size, version, and status without exposing confidential information unnecessarily.

## Source files

Editable source files, linked assets, fonts, generated assets, exports, proofs, and approvals should be managed according to project policy and license restrictions.

## Version control

Material revisions should preserve version, owner, date, purpose, changed content, changed assets, approval state, and supersession status.

## Change impact

A small copy change can alter line breaks, hierarchy, accessibility, localization, pagination, or production. Asset replacement can change licensing, crop, resolution, consent, or brand meaning. Material changes should trigger appropriate re-review.

## Approval states

Useful states can include draft, internal review, accessibility review, brand review, legal or rights review, production review, approved support package, released, superseded, and archived.

## Qualified approval

The policy requires `qualified_design_approval`. Passing automated checks does not itself authorize publication or production.

## Asset licensing authority

`approve_asset_license` is protected. F134 can track license evidence and restrictions but cannot make binding legal determinations about ownership or permitted use.

## Final brand authority

`approve_final_brand_use` is protected. Brand owners or delegated approvers retain authority over final public brand representation.

## Publication

`publish_design` is protected. F134 can prepare a reviewed package but cannot autonomously publish the design.

## Public deployment

`deploy_public_creative` is protected. Uploading or activating public creative remains a human-controlled action.

## External distribution

`external_distribution` is protected. The system cannot autonomously email, post, upload, transmit, or distribute final creative outside the governed environment.

## Confidentiality

Unreleased campaigns, product information, customer data, pricing, strategy, source files, credentials, and internal reviews can be confidential. F134 should minimize unnecessary exposure.

## Security

Production systems should use least privilege, access controls, secure asset storage, audit logs, and appropriate handling of licensed and confidential files.

## Memory and state

The `memory/` layer can preserve structured design state across agents. It should distinguish approved requirements, proposals, rejected concepts, content, assets, licenses, accessibility findings, brand state, production state, and approvals.

## Observability

The `observability/` layer supports traceability across brief, concept, layout, accessibility, rights, brand, quality, and governance states.

Useful telemetry includes deliverable version, asset inventory, provenance state, accessibility findings, unresolved brand issues, production checks, approvals, and protected-action attempts.

## Required reviews

The executable policy requires all eight conditions:

```text
brief_reviewed
concept_reviewed
layout_reviewed
accessibility_reviewed
rights_provenance_reviewed
brand_content_reviewed
quality_reviewed
qualified_design_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- copyright, plagiarism, or excessive similarity risk remains unresolved
- asset, image, illustration, or font licensing is incomplete
- material accessibility or legibility requirements remain unresolved
- brand, endorsement, affiliation, or trademark use is misleading or unresolved
- privacy, likeness, consent, or real-person imagery risk remains unresolved
- deceptive or materially misleading visual design remains unresolved
- required production or preflight quality is incomplete
- material content or asset provenance is incomplete
- any required review is missing
- qualified human design approval is missing

The system exposes blockers instead of manufacturing permission, accessibility, brand approval, or production readiness.

## Protected actions

The safety policy permanently protects:

```text
publish_design
send_to_print
approve_asset_license
approve_final_brand_use
deploy_public_creative
external_distribution
```

These actions remain outside autonomous authority even after all required reviews are satisfied.

## Human authority boundaries

F134 must not autonomously publish creative, send files to printers, approve licenses, authorize trademark use, approve final brand representation, deploy advertisements, disclose confidential assets, or distribute designs externally.

Qualified humans retain control over creative direction, rights, accessibility acceptance, brand approval, factual and legal content, production, publication, and distribution.

## Explicit failure states

```text
BRIEF REVIEW REQUIRED
CONCEPT REVIEW REQUIRED
LAYOUT REVIEW REQUIRED
ACCESSIBILITY REVIEW REQUIRED
RIGHTS OR PROVENANCE REVIEW REQUIRED
BRAND OR CONTENT REVIEW REQUIRED
QUALITY REVIEW REQUIRED
COPYRIGHT OR SIMILARITY RISK
ASSET LICENSE GAP
ACCESSIBILITY FAILURE
BRAND MISREPRESENTATION
PRIVACY OR LIKENESS RISK
DECEPTIVE DESIGN RISK
PRODUCTION QUALITY GAP
CONTENT PROVENANCE GAP
QUALIFIED DESIGN APPROVAL REQUIRED
DESIGN PUBLICATION PROHIBITED
PRINT RELEASE PROHIBITED
AUTONOMOUS LICENSE APPROVAL PROHIBITED
AUTONOMOUS BRAND APPROVAL PROHIBITED
PUBLIC CREATIVE DEPLOYMENT PROHIBITED
EXTERNAL DISTRIBUTION PROHIBITED
```

## End-to-end reference workflow

1. Parse the brief, audience, objective, content, deliverables, channels, and constraints.
2. Register required assets, brand rules, accessibility requirements, production requirements, and approval owners.
3. Develop original visual concepts and document rationale.
4. Build hierarchy, grid, typography, imagery, color, and responsive variants.
5. Review legibility, contrast, reading order, redundancy, localization, and accessibility.
6. Verify source assets, font and image licensing, consent, likeness, attribution, and provenance.
7. Review factual content, brand integrity, trademarks, disclosures, and deceptive-design risks.
8. Preflight final deliverables for channel-specific quality and production requirements.
9. Preserve versions, changed assets, approvals, unresolved risks, and provenance.
10. Apply fail-closed governance and require qualified human design approval.
11. Keep publication, print release, license approval, final brand approval, public deployment, and external distribution outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test brief interpretation, concept relevance, hierarchy and layout reasoning, accessibility awareness, asset provenance, brand integrity, production quality, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved support release, copyright similarity, asset licensing, accessibility, brand misrepresentation, privacy or likeness, deceptive design, production quality, and provenance.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed reference workflow.

## Reproducibility

Reproducible design review requires preserving brief version, concept state, layout specifications, typography, color definitions, asset inventory, licenses, source provenance, accessibility findings, brand state, production specifications, exports, approvals, and supersession state.

## Extension points

Organization-specific implementations can add governed integrations for design tools, digital-asset management, brand libraries, font systems, stock providers, accessibility checkers, proofing platforms, print vendors, content systems, and campaign platforms.

Any integration capable of publishing, printing, licensing, deploying, or externally distributing creative should remain behind explicit authorization, least privilege, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include brand collateral, editorial layouts, posters, reports, presentations, social graphics, campaign systems, infographics, packaging support, signage, multilingual creative, accessibility review, design QA, and production preflight.

F134 is not an autonomous art director, rights authority, trademark counsel, accessibility certifier, printer, advertising publisher, or brand approver.

## Design principles

1. Solve the communication problem before decorating the artifact.
2. Preserve hierarchy, legibility, accessibility, and audience context.
3. Create original expression and preserve asset provenance.
4. Never fabricate licenses, permissions, endorsements, consent, or brand approval.
5. Treat fonts, images, illustrations, trademarks, and likenesses as governed assets.
6. Reject materially deceptive visual framing and dark patterns.
7. Review the actual final deliverable, not only the editable source.
8. Fail closed when rights, accessibility, quality, provenance, or approval is incomplete.
9. Keep publication, licensing, production, and public deployment under qualified human control.

## Scope statement

F134 demonstrates a governed multi-agent architecture for graphic-design decision support. It combines specialized brief, concept, layout, accessibility, and review agents with deterministic brief, concept, grid, accessibility, and review tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over rights, brand approval, production, publication, and external distribution.

Author: Mahsa Keikha
