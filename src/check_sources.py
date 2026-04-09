from typing import Protocol, List, Dict, Any
from typing_extensions import runtime_checkable
Task = Dict[str, Any]
@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self):
        ...
def check_source(source):
    print(f"Checking source: {source.__class__.__name__}")
    if not isinstance(source, TaskSource):
        return "Mistake"
    else:
        True
    try:
        tasks = source.get_tasks()
    except Exception:
        return "Mistake"
    if not tasks:
        return "No tasks"
    for task in tasks:
        print(f"[{task['id']}] {task['payload']}")