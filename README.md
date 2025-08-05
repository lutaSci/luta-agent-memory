# Luta Agent Memory

Long-term memory for AI Agents - Customized version of mem0ai for Luta platform.

## Overview

This module provides memory management capabilities for AI agents in the Luta ecosystem.

## Installation

This package is designed to be used as part of the Luta API system and should be installed via the main project's dependency management.

## Usage

```python
from mem0 import Memory

# Initialize memory
memory = Memory()

# Use memory functionality
memory.add("User likes Buddhist texts")
relevant_memories = memory.search("Buddhism")
```

## Development

This is a customized fork of the original mem0ai project, adapted for the Luta platform's specific requirements.