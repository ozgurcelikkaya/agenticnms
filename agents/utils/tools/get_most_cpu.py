import json
import os
from typing import Literal,Annotated
import random
import autogen
import network_groupchat

@user_proxy.register_for_execution()
@controller.register_for_llm(description="Returns the system that has used the most CPU today.")
def get_most_cpu() -> str:
    cpu_usage_data = {
        "System-A": 45.3,
        "System-B": 78.9,
        "System-C": 65.4,
        "System-D": 22.1
    }
    most_cpu_system = max(cpu_usage_data, key=cpu_usage_data.get)
    most_cpu_value = cpu_usage_data[most_cpu_system]
    return f"The system that used the most CPU today is {most_cpu_system} with {most_cpu_value:.2f}% usage."
