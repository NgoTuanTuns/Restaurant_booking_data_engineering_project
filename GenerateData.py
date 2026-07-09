import random
import datetime
FOOD_TYPES = [
    "Trái cây",
    "Rau củ",
    "Thịt",
    "Hải sản",
    "Đồ uống",
    "Snack / Ăn vặt",
    "Ngũ cốc & Tinh bột",
    "Món chay",
    "Đồ nướng / BBQ",
    "Lẩu / Canh",
    "Món chính Việt Nam",
    "Món chính Châu Á",
    "Món chính Phương Tây",
    "Món tráng miệng"
]

FOOD = {
    "Trái cây": [
        "Xoài", "Chuối", "Cam", "Quýt", "Bưởi", "Dưa hấu", "Dứa", "Đu đủ",
        "Sầu riêng", "Măng cụt", "Chôm chôm", "Vải thiều", "Nhãn", "Mít",
        "Thanh long", "Ổi", "Táo", "Lê", "Nho", "Dâu tây", "Việt quất",
        "Kiwi", "Đào", "Mận", "Bơ", "Dừa", "Me", "Cóc", "Khế", "Mãng cầu",
    ],
    "Rau củ": [
        "Rau muống", "Cải xanh", "Cải thìa", "Bắp cải", "Súp lơ xanh",
        "Súp lơ trắng", "Cà rốt", "Khoai tây", "Khoai lang", "Bí đỏ",
        "Bí xanh", "Cà chua", "Dưa leo", "Cà tím", "Hành tây", "Tỏi",
        "Gừng", "Ớt chuông", "Nấm rơm", "Nấm kim châm", "Rau dền",
        "Rau ngót", "Đậu bắp", "Su su", "Giá đỗ", "Măng tươi", "Củ cải",
        "Su hào", "Rau mồng tơi", "Đậu cô ve",
    ],
    "Thịt": [
        "Thịt heo ba chỉ", "Thịt heo nạc", "Sườn heo", "Thịt bò", "Bắp bò",
        "Thịt gà ta", "Đùi gà", "Cánh gà", "Thịt vịt", "Thịt bê",
        "Thịt cừu", "Chân giò", "Thịt xông khói", "Xúc xích", "Thịt dê",
        "Nội tạng (gan, tim, cật)",
    ],
    "Hải sản": [
        "Cá hồi", "Cá basa", "Cá thu", "Cá ngừ", "Cá lóc", "Tôm sú",
        "Tôm thẻ", "Cua biển", "Ghẹ", "Mực ống", "Mực nang", "Bạch tuộc",
        "Nghêu", "Sò huyết", "Ốc hương", "Hàu", "Cá diêu hồng", "Cá trắm",
    ],
    "Món chính Việt Nam": [
        "Phở bò", "Phở gà", "Bún chả", "Bún bò Huế", "Bún riêu",
        "Cơm tấm sườn bì chả", "Bánh mì thịt", "Gỏi cuốn", "Chả giò",
        "Bánh xèo", "Bánh cuốn", "Hủ tiếu Nam Vang", "Mì Quảng",
        "Cao lầu", "Bánh canh cua", "Cơm gà Hội An", "Bún thịt nướng",
        "Canh chua cá lóc", "Thịt kho tàu", "Cá kho tộ",
    ],
    "Món chính Châu Á": [
        "Sushi", "Sashimi", "Ramen", "Udon", "Tempura", "Mì xào Singapore",
        "Cơm chiên Dương Châu", "Kim chi jjigae", "Bibimbap", "Tteokbokki",
        "Pad Thai", "Tom Yum", "Som Tum", "Dim sum", "Vịt quay Bắc Kinh",
        "Char Kway Teow", "Nasi Goreng", "Rendang", "Curry Ấn Độ",
        "Biryani", "Naan",
    ],
    "Món chính Phương Tây": [
        "Pizza Margherita", "Pasta Carbonara", "Spaghetti Bolognese",
        "Burger bò phô mai", "Steak bò Úc", "Bít tết cừu", "Risotto",
        "Lasagna", "Fish and chips", "Sandwich kẹp gà", "Salad Caesar",
        "Mac and cheese", "Tacos", "Burrito", "Paella",
    ],
    "Món tráng miệng": [
        "Chè đậu xanh", "Chè ba màu", "Bánh flan", "Rau câu", "Chè bưởi",
        "Bánh su kem", "Tiramisu", "Bánh chocolate", "Kem vani",
        "Bánh cheesecake", "Bánh táo", "Macaron", "Bánh trung thu",
        "Bánh bông lan trứng muối", "Pudding xoài", "Yaourt",
    ],
    "Đồ uống": [
        "Cà phê sữa đá", "Cà phê đen", "Trà sữa trân châu", "Trà đào",
        "Nước ép cam", "Sinh tố bơ", "Sinh tố xoài", "Nước dừa",
        "Nước mía", "Soda chanh muối", "Bia", "Rượu vang đỏ",
        "Trà gừng", "Matcha latte", "Cacao nóng", "Nước suối",
    ],
    "Snack / Ăn vặt": [
        "Bánh tráng trộn", "Cá viên chiên", "Khô bò", "Bánh phồng tôm",
        "Snack khoai tây", "Hạt điều rang", "Hạt dẻ cười", "Bỏng ngô",
        "Kẹo dẻo", "Socola", "Bánh quy", "Trái cây sấy", "Nem chua",
        "Chân gà sả tắc", "Xoài lắc",
    ],
    "Ngũ cốc & Tinh bột": [
        "Gạo tẻ", "Gạo nếp", "Yến mạch", "Bánh mì", "Bún", "Phở khô",
        "Mì gói", "Bột mì", "Bắp ngô", "Khoai môn", "Hạt quinoa",
        "Bánh tráng", "Miến", "Nui",
    ],
    "Món chay": [
        "Đậu hũ sốt cà", "Canh rau củ chay", "Chả giò chay", "Phở chay",
        "Cơm chiên chay", "Bún riêu chay", "Salad rau củ", "Nấm xào chay",
        "Đậu hũ chiên giòn", "Súp bí đỏ",
    ],
    "Đồ nướng / BBQ": [
        "Sườn nướng BBQ", "Thịt heo nướng", "Bò nướng lá lốt",
        "Gà nướng mật ong", "Tôm nướng muối ớt", "Mực nướng sa tế",
        "Cá nướng giấy bạc", "Chân gà nướng", "Xiên que nướng",
        "Bắp nướng mỡ hành",
    ],
    "Lẩu / Canh": [
        "Lẩu thái", "Lẩu hải sản", "Lẩu gà lá giang", "Lẩu bò",
        "Lẩu nấm", "Canh chua", "Canh khổ qua", "Canh bí đỏ",
        "Canh rong biển", "Súp cua",
    ],
}
TABLE_TYPES = ['Bình thường', 'Riêng tư', 'VIP', 'VVIP', 'Ngoài trời']
CLIENT_NAME = ['Tú', 'Tuấn', 'Phát', 'Quân', 'Tài', 'Sang', 'Việt']
def generate_data():
    booking_table = {}

    booking_table['Client_Name'] = random.choice(CLIENT_NAME)

    booking_table['Table_Types'] = random.choice(TABLE_TYPES)

    #Generate time for the table
    booking_year = datetime.date.today().year
    booking_month = random.randint(datetime.date.today().month, 12)
    start_date = 1
    if booking_month == datetime.date.today().month:
        start_date = datetime.date.today().day
    
    end_date = 30
    if booking_month in [1,3,5,7,8,10,12]:
        end_date = 31
    
    booking_date = random.randint(start_date, end_date)
        
    booking_table['Time'] = str(datetime.datetime(
        year = booking_year,
        month = booking_month,
        day = booking_date,
        hour = random.randint(8, 22),
        minute = random.randint(0, 59)
    ))

    #Generate number of person for the table    
    num_of_individuals = random.randint(1,7)
    booking_table['Num_Of_Individuals'] = num_of_individuals

    #Generate food for the table
    number_of_food_types = random.randint(1,10)
    food_types_for_that_table = random.sample(FOOD_TYPES, number_of_food_types)
    orderfood = {}
    for i in food_types_for_that_table:
        food_items = random.sample(FOOD.get(i), random.randint(1,num_of_individuals))
        orderfood[i] = food_items
    
    booking_table['Order'] = orderfood

    booking_table['Is_Birthdate'] = random.choice([True, False])
    return booking_table


