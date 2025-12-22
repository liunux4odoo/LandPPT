import openai
import requests


# client = openai.Client(
#     api_key="sk-6WJdvb8h1GxqROgblCAsi2ZHmbdntBDAh9bDkdsJld6XQjpj",
#     base_url="http://127.0.0.1:3000/v1",
# )

# img = client.images.generate(prompt="小桥流水人家", model="Q_IMG")

# print(img)


resp = requests.post(
    # "http://127.0.0.1:3000/v1/images/generations",
    # headers={
    #     "Authorization": f"Bearer sk-6WJdvb8h1GxqROgblCAsi2ZHmbdntBDAh9bDkdsJld6XQjpj",
    #     "Content-Type": "application/json"
    # },
    "http://10.60.253.101:3000/v1/images/generations",
    headers={
        "Authorization": f"Bearer sk-F99T5dzbZ0vo6vA6E5C68f6a16E6461c8d29A5E186A800F1",
        "Content-Type": "application/json"
    },
    json={
        "model": "Q_IMG",
        "prompt": '首先，任务是作为专业的AI图片生成提示词专家，为PPT幻灯片生成高质量的英文图片生成提示词。输出必须是英文提示词，不超过120词，直接输出，不要添加任何其他内容。\n\n关键信息回顾：\n\n- **主题**：水巷吴韵·三日探古（Water Alley Wu Charm · Three-Day Ancient Exploration）\n\n- **场景**：general\n\n- **当前页**：1/12（封面页）\n\n- **幻灯片信息**：\n\n  - 标题：封面：水巷吴韵·三日探古\n\n  - 内容：千年水乡的文化基因、园林艺术的东方密码、三日深度沉浸体验\n\n- **图片需求信息**：\n\n  - 用途：background（背景图）\n\n  - 描述：江南水乡小桥流水、古典园林的背景图，体现\'水巷吴韵\'主题\n\n  - 优先级：5\n\n  - 当前是第1张图片\n\n- **当前PPT模板HTML参考**：描述了清新风PPT模板，使用了原生CSS，风格是clean, modern, professional presentation style。\n\n- **风格指导**：general（clean, modern, professional presentation style）\n\n- **用途指导**：background（淡雅、不干扰前景内容）\n\n- **要求**：\n\n  1. 生成详细的英文提示词。\n\n  2. 根据项目场景、图片用途和模板风格选择合适的风格。\n\n  3. 包含具体的视觉元素描述。\n\n  4. 确保图片适合PPT演示使用。\n\n  5. 考虑16:9或4:3的横向构图。\n\n  6. 避免包含文字内容。\n\n  7. 由于是第1张图片，确保风格一致但内容有所区别（但因为是封面，内容会独特）。\n\n**分析**：\n\n- 主题：江南水乡，强调“水巷”（water alley）和“吴韵”（Wu charm，指吴文化，江南地区），所以图片应体现典型的江南水乡景色，如小桥、流水、古典园林。\n\n- 用途：background，所以图片应该是淡雅的背景，不抢夺标题内容（标题是“水巷吴韵·三日探古”），不能有文字。\n\n- 风格：general，具体是clean, modern, professional presentation style，符合PPT模板的清新风。\n\n- 构图：16:9横向构图，适合PPT。\n\n- 视觉元素：需要包括小桥流水、古典园林。具体描述：小桥（stone bridge）、流水（calm water with ripples）、古典园林元素（like traditional Chinese garden with pavilions, bamboo, lotus ponds）。避免现代元素，保持传统。\n\n- 其他：体现“千年水乡的文化基因”和“园林艺术的东方密码”，所以要突出文化感。\n\n**构建提示词**：\n\n- 英文提示词，简洁，详细。\n\n- 不超过120词。\n\n- 包含：16:9宽屏，江南水乡背景，小桥流水，古典园林，淡雅色调（避免太鲜艳），无文字。\n\n- 具体元素：例如，"a serene Jiangnan water town scene with a stone bridge over a tranquil stream, traditional Chinese garden with bamboo and lotus ponds, soft morning light, muted colors, clean composition for background use."\n\n- 确保符合general风格：clean, modern, professional.\n\n- 优先级5，但提示词不需要体现优先级。\n\n**草拟提示词**：\n\n"An elegant 16:9 background image of a tranquil Jiangnan water village: a classic stone bridge arching over a calm stream, surrounded by traditional Chinese garden elements like bamboo groves, lotus ponds, and ancient pavilions. Soft morning light, muted pastel colors, minimalistic composition, no text, designed for professional presentation as a subtle backdrop for \'Water Alley Wu Charm\' theme."\n\n检查词数：大约60词，符合要求。\n\n- 确保不包含文字：是的。\n\n- 横向构图：指定16:9。\n\n- 具体视觉元素：stone bridge, stream, bamboo, lotus ponds, pavilions.\n\n- 风格：elegant, serene, muted colors, clean composition – matches general style.\n\n- 用途：background, subtle backdrop.\n\n- 词数：精炼在120词内。\n\n**优化**：\n\n精炼一下：\n\n"A serene 16:9 background image depicting a Jiangnan water town: a stone bridge over a gentle stream, with traditional Chinese garden features including bamboo, lotus flowers, and a small pavilion. Soft, pastel tones, minimal details, no text, elegant and professional for PPT use."\n\n词数：约40词。\n\n确保体现"水巷吴韵"：water alley (water lane) and Wu charm.\n\n"水巷" 是 water alley, so include "water lane" or "canal".\n\n在描述中用"water town" or "water lane".\n\n"Water alley" might not be direct; better to say "Jiangnan water village with narrow canals".\n\nBut in English, it\'s common to say "Jiangnan water town".\n\nFinal prompt:\n\n"Professional 16:9 background image: a tranquil Jiangnan water village scene featuring a classic stone bridge over a calm canal, surrounded by traditional gardens with bamboo, lotus ponds, and ancient pavilions. Soft pastel colors, gentle morning light, minimalistic and elegant, no text, perfect for the \'Water Alley Wu Charm\' theme as a subtle PPT backdrop."\n\nNow, count words: let\'s see.\n\n- Professional 16:9 background image: a tranquil Jiangnan water village scene featuring a classic stone bridge over a calm canal, surrounded by traditional gardens with bamboo, lotus ponds, and ancient pavilions. Soft pastel colors, gentle morning light, minimalistic and elegant, no text, perfect for the \'Water Alley Wu Charm\' theme as a subtle PPT backdrop.\n\nWord count: about 35 words.\n\nWell under 120.\n\nEnsure it\'s English, detailed, and fits all criteria.\n\nAvoid any mention of the template or other pages; it\'s for the first slide.\n\nMake sure it\'s for background use: "subtle PPT backdrop".\n\nYes.\n\nOutput directly.\n</think>\n\nA serene 16:9 background image of a Jiangnan water village: a traditional stone bridge arching over a calm canal, surrounded by lush classical gardens with bamboo groves, lotus ponds, and ancient pavilions. Soft pastel hues, gentle morning light, minimalistic composition, no text, elegant and culturally resonant for the \'Water Alley Wu Charm\' theme, designed as a subtle, professional PPT backdrop that enhances without distracting.',
        "size": "1328x928",
        "response_format": "b64_json",
        "quality": "standard",
    }
)

print(resp.content)
