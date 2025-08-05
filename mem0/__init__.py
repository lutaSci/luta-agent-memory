# 修复元数据问题：直接设置版本，无需从包管理系统获取
__version__ = "0.1.115"

from mem0.client.main import AsyncMemoryClient, MemoryClient  # noqa
from mem0.memory.main import AsyncMemory, Memory  # noqa
