#!/bin/bash

# Bash脚本：替换文件中的字符串
# 将JSON、Python和HTML文件中的字符串"a"替换为"b"

echo "正在查找并替换文件中的字符串..."

# 查找所有JSON、Python和HTML文件
files=$(find src template_examples -type f \( -name "*.json" -o -name "*.py" -o -name "*.html" \))

# 检查是否找到文件
if [ -z "$files" ]; then
    echo "未找到任何指定类型的文件"
    exit 1
fi

# 统计文件数量
file_count=$(echo "$files" | wc -l)
echo "找到 $file_count 个文件"

# 处理每个文件
while IFS= read -r file; do
    if [ -n "$file" ]; then
        echo "处理文件: $file"
        
        # 使用sed命令替换字符串"a"为"b"
        # -i选项表示直接修改原文件
        sed -i 's|https://cdn.tailwindcss.com|/static/js/libs/tailwindcss-3.4.17.js|g' "$file"
        sed -i 's|https://cdn.jsdelivr.net/npm/chart.js|/static/js/libs/chart-4.5.0.js|g' "$file"
        sed -i 's|https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/js/all.min.js|/static/js/libs/fontawesome-6.0.0/js/all.min.js|g' "$file"
        sed -i 's|https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css|/static/js/libs/fontawesome-6.0.0/css/all.min.css|g' "$file"
        sed -i 's|https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js|/static/js/libs/fontawesome-6.0.0/js/all.min.js|g' "$file"
        sed -i 's|https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css|/static/js/libs/fontawesome-6.0.0/css/all.min.css|g' "$file"
        sed -i 's|https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js|/static/js/libs/bootstrap-5.1.3/js/bootstrap.bundle.min.js|g' "$file"
        sed -i 's|https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css|/static/css/libs/bootstrap-5.1.3/css/bootstrap.bundle.min.css|g' "$file"
        sed -i 's|https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2|/static/js/libs/codemirror-5.65.2|g' "$file"
        sed -i 's|script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js'|script.src = '/static/js/libs/html2canvas-1.4.1.min.js'|g' "$file"
    fi
done <<< "$files"

echo ""
echo "替换完成！"