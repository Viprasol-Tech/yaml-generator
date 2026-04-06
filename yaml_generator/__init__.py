"""
yaml-generator - Generate YAML config from Python objects

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import YamlGenerator, generate, process, main

__all__ = ["YamlGenerator", "generate", "process", "main"]
