"""
YAML Tools - AI YAML工具集
支持YAML生成、转换、验证
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class YAMLTools:
    """
    AI YAML工具集
    支持：生成、转换、验证、Schema
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def json_to_yaml(self, json_data: str) -> str:
        """JSON转YAML"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下JSON转换为YAML格式：

{json_data}

只返回YAML代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def yaml_to_json(self, yaml_data: str) -> str:
        """YAML转JSON"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下YAML转换为JSON格式：

{yaml_data}

只返回JSON代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_from_description(self, description: str, config_type: str = "generic") -> str:
        """从描述生成YAML"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下描述生成{config_type}配置的YAML：

描述：{description}

只返回YAML代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def validate_yaml(self, yaml_data: str) -> Dict:
        """验证YAML"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请验证以下YAML的语法和结构：

{yaml_data}

请返回JSON格式：
{{
    "valid": true/false,
    "errors": ["错误1", "错误2"],
    "warnings": ["警告1", "警告2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"validation": content}

    def generate_k8s_manifest(self, app_name: str, image: str, port: int = 80) -> str:
        """生成Kubernetes清单"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下应用生成Kubernetes部署清单：

应用名称：{app_name}
镜像：{image}
端口：{port}

请生成Deployment和Service的YAML："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_docker_compose(self, services: List[Dict]) -> str:
        """生成Docker Compose"""
        if not self.client:
            return "LLM客户端未配置"

        services_text = json.dumps(services, ensure_ascii=False, indent=2)

        prompt = f"""请根据以下服务配置生成docker-compose.yml：

{services_text}

只返回YAML代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_github_actions(self, workflow_name: str, steps: List[str]) -> str:
        """生成GitHub Actions"""
        if not self.client:
            return "LLM客户端未配置"

        steps_text = "\n".join(f"- {s}" for s in steps)

        prompt = f"""请生成GitHub Actions工作流：

名称：{workflow_name}
步骤：
{steps_text}

请生成YAML格式的工作流文件："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> YAMLTools:
    """创建YAML工具"""
    return YAMLTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("YAML Tools")
    print()

    # 测试
    result = tools.generate_k8s_manifest("my-app", "nginx:latest", 80)
    print(result[:300] + "...")
