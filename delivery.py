import datetime

# دیتابیس ما (لیست از دیکشنری‌ها)
orders = [
{"id": 1, "product": "Laptop", "order_date_time": "2025-09-10 14:20",
"status": "rejected", "deliver_date_time": None},
{"id": 2, "product": "Phone", "order_date_time": "2025-09-12 09:10",
"status": "send", "deliver_date_time": None},
{"id": 3, "product": "Book", "order_date_time": "2025-09-13 11:40",
"status": "delivered", "deliver_date_time": "2025-09-14 18:00"},
{"id": 4, "product": "Headphones", "order_date_time": "2025-09-14 19:30",
"status": "rejected", "deliver_date_time": None}
]

# ---------- توابع ----------
def show_rejected():
print("\n📦 کالاهای ریجکت شده:")
for order in orders:
if order["status"] == "rejected":
print(order)

def show_sent():
print("\n🚚 کالاهای ارسال‌شده:")
for order in orders:
if order["status"] == "send":
print(order)

def add_order(product):
new_id = len(orders) + 1
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
orders.append({
"id": new_id,
"product": product,
"order_date_time": now,
"status": "none",
"deliver_date_time": None
})
print(f"✅ سفارش جدید با id={new_id} اضافه شد.")

# ---------- اجرای برنامه ----------
print("=== سیستم ثبت دلیوری ===")

# وقتی برنامه باز میشه → فقط rejected ها
show_rejected()

while True:
print("\nمنو:")
print("1. افزودن سفارش جدید")
print("2. نمایش کالاهای ارسال‌شده (send)")
print("3. خروج")

choice = input("انتخاب کن: ")

if choice == "1":
product = input("نام کالا: ")
add_order(product)
elif choice == "2":
show_sent()
elif choice == "3":
print("خداحافظ ✌️")
break
else:
print("گزینه نامعتبر ❌")