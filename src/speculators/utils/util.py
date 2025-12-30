def is_npu_available() ->  bool:
    """Detect Ascend NPU availability"""
    try:
        from transformers.utils import is_torch_npu_available

        return is_torch_npu_available()
    except Exception:
        return False