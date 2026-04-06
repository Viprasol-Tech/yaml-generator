# Yaml Generator

Generate YAML config from Python objects

## Features

- Zero external dependencies (stdlib only)
- Easy-to-use CLI interface
- Professional Python implementation
- MIT licensed

## Installation

```bash
pip install -e .
```

Or clone and install:

```bash
git clone https://github.com/Viprasol-Tech/yaml-generator
cd yaml-generator
pip install -e .
```

## Usage

### Python

```python
from yaml_generator import YamlGenerator

result = YamlGenerator.process("data")
print(result)
```

### CLI

```bash
python -m yaml_generator "your input here"
```

## Documentation

See the source code and docstrings for detailed API documentation.

## License

MIT License - see LICENSE file for details

## About

Part of Viprasol Utilities: https://viprasol.com

Created by Viprasol - Building AI-focused tools for developers.
