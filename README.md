# 📄 YAML Tools

AI YAML工具集，支持YAML生成、转换、验证。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🔄 JSON/YAML互转
- 📝 从描述生成YAML
- ✅ YAML验证
- ☸️ Kubernetes清单生成
- 🐳 Docker Compose生成
- 🔄 GitHub Actions生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from yaml_tools import create_tools

tools = create_tools()

# JSON转YAML
yaml = tools.json_to_yaml('{"name": "test"}')

# YAML转JSON
json_data = tools.yaml_to_json(yaml)

# 生成K8s清单
k8s = tools.generate_k8s_manifest("my-app", "nginx:latest", 80)

# 生成Docker Compose
compose = tools.generate_docker_compose([
    {"name": "web", "image": "nginx"},
    {"name": "api", "image": "node:18"}
])

# 生成GitHub Actions
actions = tools.generate_github_actions("CI/CD", ["checkout", "build", "test", "deploy"])
```

## 📁 项目结构

```
yaml-tools/
├── tools.py       # YAML工具核心
└── README.md
```

## 📄 许可证

MIT License
