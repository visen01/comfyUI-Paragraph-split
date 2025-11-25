class TextParagraphSplitter:
    """
    文本段落分割器 - 将输入文本按空行分割为多个段落
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,  # 支持多行文本输入
                    "placeholder": "输入需要分割段落的文本..."
                }),
                "trim_whitespace": ("BOOLEAN", {
                    "default": True,
                    "label_on": "去除首尾空格",
                    "label_off": "保留原始空格"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING", "LIST",)
    RETURN_NAMES = ("段落文本拼接", "段落列表",)
    FUNCTION = "split_paragraphs"
    CATEGORY = "文本处理/段落分割"

    def split_paragraphs(self, text, trim_whitespace):
        # 处理空输入
        if not text:
            return ("", [],)
        
        # 按换行符分割成行
        lines = text.split('\n')
        
        paragraphs = []
        current_paragraph = []
        
        for line in lines:
            # 根据设置决定是否去除行首尾空格
            processed_line = line.strip() if trim_whitespace else line
            
            # 空行表示段落结束
            if not processed_line:
                if current_paragraph:
                    # 将当前段落的所有行合并
                    paragraph = ' '.join(current_paragraph) if trim_whitespace else '\n'.join(current_paragraph)
                    paragraphs.append(paragraph)
                    current_paragraph = []
            else:
                current_paragraph.append(processed_line)
        
        # 处理最后一个段落
        if current_paragraph:
            paragraph = ' '.join(current_paragraph) if trim_whitespace else '\n'.join(current_paragraph)
            paragraphs.append(paragraph)
        
        # 拼接所有段落实例（用两个换行符分隔）
        joined_paragraphs = '\n\n'.join(paragraphs)
        
        return (joined_paragraphs, paragraphs,)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "TextParagraphSplitter": TextParagraphSplitter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextParagraphSplitter": "🔵BB文本段落分割器(列表)"
}
