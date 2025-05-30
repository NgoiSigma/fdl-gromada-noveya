# 📘 FDL LANGUAGE SPECIFICATION

The FDL (Formal-Dialectical Logic) language is a symbolic and semantically-aware programming and coordination language for expressing intention, logic, flow, and transformation within collective reasoning systems.

This document outlines the syntax and structural rules of the FDL language.

---

## 🔹 SYNTAX OVERVIEW

FDL operates in **phases** and **flows**, where each block encapsulates:

* **Initiation** → declaration of context or intention
* **Expansion** → unfolding the domain or parameters
* **Tension** → resolving contradictions or oppositions
* **Synthesis** → constructing the integrated outcome

### 🧱 Block structure example:

```fdl
@block "DecisionLogic::ResourceAllocation"
init:
  intent: "optimize resource distribution based on ethical priority"

expand:
  if region == "critical" then priority = "high"
  else priority = "moderate"

tension:
  check: region_priority conflicts with budget_limit
  resolve: adjust priority dynamically

synthesize:
  output: final_distribution_scheme
```

---

## 🔹 KEYWORDS

| Keyword      | Function                                       |
| ------------ | ---------------------------------------------- |
| `@block`     | Declares a named FDL logic unit                |
| `init`       | Sets the intention and origin                  |
| `expand`     | Defines variables, domain logic, or conditions |
| `tension`    | Encodes contradictions or dialectical tests    |
| `synthesize` | Resolves and finalizes the semantic action     |

---

## 🔹 SEMANTIC MARKERS

FDL supports inner semantic labels to track:

* `::` domain path or resonance lineage
* `#tag` thematic tags for clustering
* `@meta:` for internal notes or linkages

---

## 🔹 VALIDATION RULES

1. Each `@block` must contain at least `init` and `synthesize`.
2. Identifiers must follow snake\_case or CamelCase conventions.
3. Semantic lineage (`::`) must be unique per module.
4. Contradictions in `tension` must either be resolved or explicitly deferred.

---

## 🔹 EXAMPLES & EXTENSIONS

Additional advanced features (loops, agents, parallel states) are defined in the `fdl_macro_patterns.fdl` file and through API invocation via `gromada_live_api.py`.

---

> "FDL doesn’t just execute — it listens, reflects, and then acts."
