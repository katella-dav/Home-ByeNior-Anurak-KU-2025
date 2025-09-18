import os

def generate_html_table_from_folder(folder_path, per_row=4, width=150):
    """
    สร้าง HTML table จากไฟล์ในโฟลเดอร์
    - folder_path: path ของโฟลเดอร์ที่มีรูป
    - per_row: จำนวนรูปต่อแถว
    - width: ความกว้างรูป (px)
    """
    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg','.png'))])
    html = '<table>\n'

    for i, file_name in enumerate(files):
        if i % per_row == 0:
            html += '  <tr>\n'

        html += f'    <td><img src="./{file_name}" width="{width}"><br><a href="./{file_name}">{file_name}</a></td>\n'

        if (i + 1) % per_row == 0:
            html += '  </tr>\n'

    # ปิดแถวสุดท้ายถ้าไม่ครบ per_row
    if len(files) % per_row != 0:
        html += '  </tr>\n'

    html += '</table>'
    return html

# ตัวอย่างใช้งาน
folder = "Freshmen (KU85)"   # โฟลเดอร์ที่มีไฟล์รูป
html_table = generate_html_table_from_folder(folder)

# เขียนไฟล์ HTML
with open("Freshmen.html", "w", encoding="utf-8") as f:
    f.write(html_table)

print("HTML table สำหรับ Freshmen สร้างเรียบร้อยแล้ว!")
