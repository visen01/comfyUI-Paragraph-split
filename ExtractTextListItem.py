class ExtractTextListItem:
    """
    从文本列表中提取指定索引的项并输出，其他项不输出
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_list": ("LIST", {"default": [], "description": "要处理的文本列表"}),
                "index": ("INT", {"default": 0, "min": 0, "description": "要提取的项的索引（从0开始）"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("extracted_text",)
    FUNCTION = "extract_item"
    CATEGORY = "文本处理"

    def extract_item(self, text_list, index):
        # 检查输入是否为有效列表
        if not isinstance(text_list, list):
            return ("",)  # 非列表时返回空字符串
        
        # 检查索引是否在有效范围内
        if index < 0 or index >= len(text_list):
            return ("",)  # 索引无效时返回空字符串
        
        # 获取指定索引的项
        extracted_item = text_list[index]
        
        # 确保输出为字符串类型
        if not isinstance(extracted_item, str):
            extracted_item = str(extracted_item)
            
        return (extracted_item,)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "ExtractTextListItem": ExtractTextListItem
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExtractTextListItem": "🔵BB提取文本列表项"
}