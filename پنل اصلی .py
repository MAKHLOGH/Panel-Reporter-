from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# ========== منوی اصلی ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(text="⚙️ تنظیمات اکانت", callback_data="account_settings"),
            InlineKeyboardButton(text="📊 گزارشات", callback_data="reports")
        ],
        [
            InlineKeyboardButton(text="📋 لیست گزارشات", callback_data="report_list"),
            InlineKeyboardButton(text="👤 ادمین و مالک", callback_data="admin_settings")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text("سلام! لطفاً یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=reply_markup)
    else:
        query = update.callback_query
        await query.edit_message_text("سلام! لطفاً یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=reply_markup)

# ========== منوی گزارشات ==========
async def show_reports_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(text="📢 ریپورت چنل", callback_data="report_channel"),
            InlineKeyboardButton(text="💬 ریپورت گپ", callback_data="report_group")
        ],
        [
            InlineKeyboardButton(text="👤 ریپورت اکانت", callback_data="report_user"),
            InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("لطفاً نوع گزارش را انتخاب کنید:", reply_markup=reply_markup)

# ========== لیست اصلی دلایل ==========
async def show_channel_report_reasons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reasons = [
        ("خشونت", "main_violence"),
        ("کالاها و خدمات غیر مجاز", "main_illegal_goods"),
        ("محتوای بزرگسالان غیر مجاز", "main_adult_content"),
        ("داده‌های شخصی", "main_personal_data"),
        ("کلاهبرداری یا تقلب", "main_fraud"),
        ("حق تکثیر", "main_copyright"),
        ("هرزنامه", "main_spam"),
        ("دیگر", "main_other")
    ]
    keyboard = [[InlineKeyboardButton(text=t, callback_data=cb)] for t, cb in reasons]
    keyboard.append([InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_reports_menu")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("دلیل گزارش را انتخاب کنید:", reply_markup=reply_markup)

# ========== زیرمنوها (کامل) ==========

# --- خشونت ---
async def show_violence_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reasons = [
        ("اهانت یا اطلاعات نادرست", "v_insult"),
        ("محتوای خشونت‌آمیز گرافیکی یا ناراحت‌کننده", "v_graphic"),
        ("خشونت شدید مثله‌کردن", "v_extreme"),
        ("نفرت‌پراکنی یا نمادهای نفرت", "v_hate"),
        ("تشویق به خشونت", "v_incite"),
        ("جرائم سازمان‌یافته", "v_organized_crime"),
        ("تروریسم", "v_terrorism"),
        ("حیوان‌آزاری", "v_animal_abuse")
    ]
    keyboard = [[InlineKeyboardButton(text=t, callback_data=cb)] for t, cb in reasons]
    keyboard.append([InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main_reasons")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("زیرمجموعه خشونت:", reply_markup=reply_markup)

# --- کالاهای غیرمجاز ---
async def show_illegal_goods_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reasons = [
        ("سلاح‌ها", "ig_weapons"),
        ("مواد مخدر", "ig_drugs"),
        ("سندهای جعلی", "ig_fake_documents"),
        ("پول تقلبی", "ig_counterfeit_money"),
        ("ابزارهای هک کننده و نرم‌افزارهای مخرب", "ig_hacking_tools"),
        ("کالاهای جعلی", "ig_counterfeit_goods"),
        ("سایر محصولات و خدمات", "ig_other_goods")
    ]
    keyboard = [[InlineKeyboardButton(text=t, callback_data=cb)] for t, cb in reasons]
    keyboard.append([InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main_reasons")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("زیرمجموعه کالاها و خدمات غیرمجاز:", reply_markup=reply_markup)

# --- محتوای بزرگسالان ---
async def show_adult_content_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reasons = [
        ("تصاویر جنسی بزرگسال دارای حق نشر", "ac_copyrighted_adult"),
        ("کودک‌آزاری", "ac_child_abuse"),
        ("خدمات جنسی غیرقانونی", "ac_illegal_sex_services"),
        ("حیوان‌آزاری", "ac_animal_abuse"),
        ("محتوای جنسی بدون رضایت", "ac_nonconsensual"),
        ("محتوای جنسی غیرقانونی دیگر", "ac_other_illegal_adult")
    ]
    keyboard = [[InlineKeyboardButton(text=t, callback_data=cb)] for t, cb in reasons]
    keyboard.append([InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main_reasons")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("زیرمجموعه محتوای بزرگسالان غیرمجاز:", reply_markup=reply_markup)

# --- داده‌های شخصی ---
async def show_personal_data_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reasons = [
        ("اسناد خصوصی", "p_private_docs"),
        ("شماره تلفن", "p_phone_number"),
        ("آدرس", "p_address"),
        ("اطلاعات یا مدارک دزدیده شده", "p_stolen_data"),
        ("اطلاعات خصوصی دیگر", "p_other_private")
    ]
    keyboard = [[InlineKeyboardButton(text=t, callback_data=cb)] for t, cb in reasons]
    keyboard.append([InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main_reasons")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("زیرمجموعه داده‌های شخصی:", reply_markup=reply_markup)

# --- کلاهبرداری ---
async def show_fraud_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reasons = [
        ("جعل هویت", "f_identity_fraud"),
        ("ادعاهای مالی فریبنده یا غیر واقعی", "f_financial_scam"),
        ("بدافزار فیشینگ", "f_phishing"),
        ("فروشنده محصول یا خدمت جعلی", "f_fake_seller")
    ]
    keyboard = [[InlineKeyboardButton(text=t, callback_data=cb)] for t, cb in reasons]
    keyboard.append([InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main_reasons")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("زیرمجموعه کلاهبرداری یا تقلب:", reply_markup=reply_markup)

# --- هرزنامه ---
async def show_spam_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reasons = [
        ("اهانت یا اطلاعات نادرست", "s_insult"),
        ("تبلیغ محتوای دیگر", "s_promotion"),
        ("تبلیغ گروه یا کانال دیگر", "s_group_promo")
    ]
    keyboard = [[InlineKeyboardButton(text=t, callback_data=cb)] for t, cb in reasons]
    keyboard.append([InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main_reasons")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("زیرمجموعه هرزنامه:", reply_markup=reply_markup)

# --- دیگر ---
async def show_other_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reasons = [
        ("به این علاقه ندارم", "o_not_interested"),
        ("اطلاعات نادرست یا تهمت", "o_false_info"),
        ("محتوای بزرگسالان غیرمجاز", "o_adult_content"),
        ("کالاها و خدمات غیرمجاز", "o_illegal_goods"),
        ("چیزی دیگر", "o_something_else")
    ]
    keyboard = [[InlineKeyboardButton(text=t, callback_data=cb)] for t, cb in reasons]
    keyboard.append([InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main_reasons")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("زیرمجموعه «دیگر»:", reply_markup=reply_markup)

# --- حق تکثیر ---
async def show_copyright_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reasons = [
        ("محتوای کپی‌شده بدون اجازه", "cr_unauthorized_copy"),
        ("نقض حق نشر موسیقی/فیلم", "cr_music_video"),
        ("دیگر موارد نقض کپی‌رایت", "cr_other")
    ]
    keyboard = [[InlineKeyboardButton(text=t, callback_data=cb)] for t, cb in reasons]
    keyboard.append([InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main_reasons")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("زیرمجموعه حق تکثیر:", reply_markup=reply_markup)

# ========== منوی نهایی ==========
async def show_report_type_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(text="📝 ریپورت با متن", callback_data="report_with_text")],
        [InlineKeyboardButton(text="🚫 ریپورت بدون متن", callback_data="report_without_text")],
        [InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main_reasons")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("نوع گزارش را انتخاب کنید:", reply_markup=reply_markup)

# ========== منوهای تنظیمات ==========
async def show_account_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(text="🗑️ حذف اکانت", callback_data="remove_account"),
            InlineKeyboardButton(text="➕ اضافه کردن اکانت", callback_data="add_account")
        ],
        [
            InlineKeyboardButton(text="📋 لیست اکانت‌ها", callback_data="list_accounts"),
            InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("تنظیمات اکانت — یکی از گزینه‌ها را انتخاب کنید:", reply_markup=reply_markup)

async def show_admin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(text="👑 اضافه کردن مالک", callback_data="add_owner"),
            InlineKeyboardButton(text="➕ اضافه کردن ادمین", callback_data="add_admin")
        ],
        [
            InlineKeyboardButton(text="📋 لیست ادمین‌ها و مالکین", callback_data="list_admins_owners"),
            InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("مدیریت دسترسی‌ها — یکی از گزینه‌ها را انتخاب کنید:", reply_markup=reply_markup)

async def show_report_list_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(text="📢 گزارش چنل و گپ", callback_data="report_channel_group")],
        [InlineKeyboardButton(text="👤 گزارش اکانت", callback_data="report_user_account")],
        [InlineKeyboardButton(text="↩️ بازگشت", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("لطفاً نوع گزارش را انتخاب کنید:", reply_markup=reply_markup)

# ========== هندلر اصلی ==========
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    if data == "back_to_main":
        await start(update, context)
        return
    elif data == "back_to_reports_menu":
        await show_reports_menu(update, context)
        return
    elif data == "back_to_main_reasons":
        await show_channel_report_reasons(update, context)
        return
    elif data == "reports":
        await show_reports_menu(update, context)
        return
    elif data == "account_settings":
        await show_account_menu(update, context)
        return
    elif data == "admin_settings":
        await show_admin_menu(update, context)
        return
    elif data == "report_list":
        await show_report_list_menu(update, context)
        return
    elif data in ["report_channel", "report_group"]:
        await show_channel_report_reasons(update, context)
        return
    elif data == "report_user":
        await query.answer()
        await query.edit_message_text("👤 ریپورت اکانت انتخاب شد.")
        return
    elif data == "report_channel_group":
        await show_channel_report_reasons(update, context)
        return
    elif data == "report_user_account":
        await query.answer()
        await query.edit_message_text("👤 گزارش اکانت انتخاب شد.")
        return

    # --- زیرمنوهای اصلی ---
    elif data == "main_violence":
        await show_violence_menu(update, context)
        return
    elif data == "main_illegal_goods":
        await show_illegal_goods_menu(update, context)
        return
    elif data == "main_adult_content":
        await show_adult_content_menu(update, context)
        return
    elif data == "main_personal_data":
        await show_personal_data_menu(update, context)
        return
    elif data == "main_fraud":
        await show_fraud_menu(update, context)
        return
    elif data == "main_spam":
        await show_spam_menu(update, context)
        return
    elif data == "main_other":
        await show_other_menu(update, context)
        return
    elif data == "main_copyright":
        await show_copyright_menu(update, context)
        return

    # --- تمام گزینه‌های نهایی ---
    elif data in [
        # خشونت
        "v_insult", "v_graphic", "v_extreme", "v_hate", "v_incite",
        "v_organized_crime", "v_terrorism", "v_animal_abuse",
        # کالاهای غیرمجاز
        "ig_weapons", "ig_drugs", "ig_fake_documents", "ig_counterfeit_money",
        "ig_hacking_tools", "ig_counterfeit_goods", "ig_other_goods",
        # محتوای بزرگسالان
        "ac_copyrighted_adult", "ac_child_abuse", "ac_illegal_sex_services",
        "ac_animal_abuse", "ac_nonconsensual", "ac_other_illegal_adult",
        # داده‌های شخصی
        "p_private_docs", "p_phone_number", "p_address", "p_stolen_data", "p_other_private",
        # کلاهبرداری
        "f_identity_fraud", "f_financial_scam", "f_phishing", "f_fake_seller",
        # هرزنامه
        "s_insult", "s_promotion", "s_group_promo",
        # دیگر
        "o_not_interested", "o_false_info", "o_adult_content", "o_illegal_goods", "o_something_else",
        # حق تکثیر
        "cr_unauthorized_copy", "cr_music_video", "cr_other"
    ]:
        await show_report_type_menu(update, context)
        return

    # --- پاسخ نهایی ---
    elif data == "report_with_text":
        await query.answer()
        await query.edit_message_text("📝 ریپورت با متن انتخاب شد.")
        return
    elif data == "report_without_text":
        await query.answer()
        await query.edit_message_text("✅ گزارش بدون متن ارسال شد.")
        return

    else:
        await query.answer()
        await query.edit_message_text("گزینه ناشناخته!")

# ========== راه‌اندازی ==========
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == '__main__':
    main()