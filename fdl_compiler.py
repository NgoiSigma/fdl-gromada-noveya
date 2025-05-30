# 🧠 FDL Compiler
# Semantic-to-logical compiler for Formal-Dialectical Logic blocks

import re
import json
from typing import Dict, List, Any

class FDLCompiler:
    def __init__(self):
        self.ast = []
        self.errors = []

    def parse_block(self, text: str) -> Dict[str, Any]:
        block = {}
        phases = ["init", "expand", "tension", "synthesize"]

        lines = text.strip().splitlines()
        current_phase = None

        for line in lines:
            line = line.strip()
            if line.startswith("@block"):
                block_name = line.split("\"")[1]
                block["name"] = block_name
                block["phases"] = {}
            elif any(line.startswith(p + ":") for p in phases):
                current_phase = line[:-1]
                block["phases"][current_phase] = []
            elif current_phase and line:
                block["phases"][current_phase].append(line)

        return block

    def validate_block(self, block: Dict[str, Any]) -> bool:
        required = ["init", "synthesize"]
        for phase in required:
            if phase not in block.get("phases", {}):
                self.errors.append(f"Missing required phase: {phase}")
                return False
        return True

    def compile(self, source_code: str) -> Dict[str, Any]:
        block = self.parse_block(source_code)
        if self.validate_block(block):
            self.ast.append(block)
            return {"status": "success", "ast": block}
        else:
            return {"status": "error", "errors": self.errors}

    def export_ast(self) -> str:
        return json.dumps(self.ast, indent=2)

# Example usage
if __name__ == "__main__":
    fdl_code = """
    @block "Example::Test"
    init:
      intent: "test logic"
    expand:
      define: A = true
    tension:
      check: A == false
    synthesize:
      result: resolved
    """
    
    compiler = FDLCompiler()
    result = compiler.compile(fdl_code)
    print(json.dumps(result, indent=2))
