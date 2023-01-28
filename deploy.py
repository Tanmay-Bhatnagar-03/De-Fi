from solcx import compile_standard
import json

with open("./simpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile Solidity

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"simpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm,bytecode", "evm.bytecode.sourceMap"]}
            }
        },
    },
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)
