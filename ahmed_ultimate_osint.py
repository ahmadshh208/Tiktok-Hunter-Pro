import requests
import re
import os
import json
from datetime import datetime

def banner():
    os.system('clear')
    print(f"""
    \033[1;31m
     █████╗ ██╗  ██╗███╗   ███╗███████╗██████╗ 
    ██╔══██╗██║  ██║████╗ ████║██╔════╝██╔══██╗
    ███████║███████║██╔████╔██║█████╗  ██║  ██║
    ██╔══██║██╔══██║██║╚██╔╝██║██╔══╝  ██║  ██║
    ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝
    \033[1;36m [!] ULTRA EDITION v6.0 | DEVELOPER: AHMED \033[0m
    """)

def get_creation_date(uid):
    try:
        # تقنية تحويل الـ ID إلى تاريخ إنشاء
        binary = bin(int(uid))
        timestamp = int(binary[2:33], 2)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    except:
        return "Unknown"

def ahmed_ultra_scan(username):
    username = username.replace('@', '').lower()
    url = f"https://www.tiktok.com/@{username}"
    
    # محاكاة متصفح حقيقي لتجنب الحظر
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Referer': 'https://www.google.com/',
    }

    print(f"\033[1;33m[*] Ahmed's Engine is Scanning: @{username}...\033[0m")
    
    try:
        res = requests.get(url, headers=headers, timeout=20)
        if res.status_code == 200:
            html = res.text
            
            # 1. استخراج الـ ID (أنماط متعددة لضمان الظهور)
            uid = "Unknown"
            patterns = [r'\"userId\":\"(\d+)\"', r'\"authorId\":\"(\d+)\"', r'\"id\":\"(\d+)\"']
            for p in patterns:
                match = re.search(p, html)
                if match:
                    uid = match.group(1)
                    break
            
            # 2. استخراج الإحصائيات (المتابعين، الإعجابات، الخ)
            def find_stat(pattern, text):
                match = re.search(pattern, text)
                return match.group(1) if match else "0"

            followers = find_stat(r'\"followerCount\":(\d+)', html)
            following = find_stat(r'\"followingCount\":(\d+)', html)
            hearts = find_stat(r'\"heartCount\":(\d+)', html)
            videos = find_stat(r'\"videoCount\":(\d+)', html)
            
            # 3. المنطقة والخصوصية
            reg_match = re.search(r'\"region\":\"([A-Z]{2})\"', html)
            region = reg_match.group(1) if reg_match else "N/A"
            is_private = "privateAccount\":true" in html
            
            # 4. تاريخ الإنشاء
            c_date = get_creation_date(uid) if uid.isdigit() else "N/A"
            
            # 5. صيد الإيميلات
            emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)))

            # --- عرض النتائج النهائية بشكل أسطوري ---
            print(f"\n\033[1;32m[✔] FULL DATA CAPTURED BY AHMED:\033[0m")
            print(f"\033[1;37m" + "━"*50 + "\033[0m")
            print(f"\033[1;37m👤 Profile:    \033[1;34m@{username}\033[0m")
            print(f"\033[1;37m🆔 User ID:    \033[1;31m{uid}\033[0m")
            print(f"\033[1;37m📅 Created:    \033[1;36m{c_date}\033[0m")
            print(f"\033[1;37m🌍 Region:     \033[1;36m{region}\033[0m")
            print(f"\033[1;37m🔒 Private:    \033[1;33m{'Yes' if is_private else 'No'}\033[0m")
            print(f"\033[1;37m" + "━"*20 + " STATS " + "━"*20 + "\033[0m")
            print(f"\033[1;32m👥 Followers:  {followers}\033[0m")
            print(f"\033[1;32m👤 Following:  {following}\033[0m")
            print(f"\033[1;32m❤️ Total Likes: {hearts}\033[0m")
            print(f"\033[1;32m🎥 Videos:      {videos}\033[0m")
            print(f"\033[1;37m" + "━"*20 + " CONTACT " + "━"*19 + "\033[0m")
            print(f"\033[1;33m📧 Emails:     {', '.join(emails) if emails else 'None Found'}\033[0m")
            print(f"\033[1;37m" + "━"*50 + "\033[0m")

            # حفظ التقرير باسم المطور أحمد
            report = {
                "developer": "AHMED",
                "target": username,
                "stats": {"followers": followers, "likes": hearts, "videos": videos},
                "info": {"id": uid, "created": c_date, "region": region}
            }
            with open(f"ahmed_report_{username}.json", "w") as f:
                json.dump(report, f, indent=4)
            print(f"\033[1;30m[Report saved: ahmed_report_{username}.json]\033[0m\n")

        else:
            print(f"\033[1;31m[-] TikTok blocked the request. Code: {res.status_code}\033[0m")
    except Exception as e:
        print(f"\033[1;31m[-] Error: {e}\033[0m")

if __name__ == "__main__":
    banner()
    inp = input("\033[1;37mEnter TikTok Username: \033[0m")
    ahmed_ultra_scan(inp)
        
        if res.status_code == 200:
            html = res.text
            
            # 1. جلب الـ ID بذكاء (أنماط متعددة)
            uid = "Not Found"
            id_patterns = [r'\"userId\":\"(\d+)\"', r'\"id\":\"(\d+)\"', r'authorId\":\"(\d+)\"']
            for pattern in id_patterns:
                match = re.search(pattern, html)
                if match:
                    uid = match.group(1)
                    break
            
            # 2. تاريخ الإنشاء (تحسين الحساب)
            c_date = "N/A"
            if uid != "Not Found":
                try:
                    ts = int(bin(int(uid))[2:33], 2)
                    c_date = datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                except: pass

            # 3. المنطقة (Region)
            reg = re.search(r'\"region\":\"([A-Z]{2})\"', html)
            region = reg.group(1) if reg else "N/A"

            # 4. السيرة الذاتية (Bio) - ميزة جديدة
            bio_match = re.search(r'\"signature\":\"(.*?)\"', html)
            bio = bio_match.group(1).encode().decode('unicode-escape') if bio_match else "No Bio"

            # 5. صيد الإيميلات (تحسين الفلترة)
            emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)))

            # --- عرض النتائج الاحترافية ---
            print(f"\n\033[1;32m[✔] Deep Scan Results:\033[0m")
            print(f"─" * 45)
            print(f"\033[1;37m👤 User:       \033[1;34m@{username}\033[0m")
            print(f"\033[1;37m🆔 ID:         \033[1;36m{uid}\033[0m")
            print(f"\033[1;37m📅 Created:    \033[1;36m{c_date}\033[0m")
            print(f"\033[1;37m🌍 Region:     \033[1;31m{region}\033[0m")
            print(f"\033[1;37m📝 Bio:        \033[1;32m{bio}\033[0m")
            print(f"\033[1;37m📧 Emails:     \033[1;33m{', '.join(emails) if emails else 'Private'}\033[0m")
            print(f"─" * 45)
            
        else:
            print(f"\033[1;31m[-] TikTok blocked the request (Status: {res.status_code})\033[0m")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    banner()
    get_data(input("Enter Target Username: "))
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    print(f"\033[1;33m[*] Ahmed's Engine is Scanning: @{username}...\033[0m")
    
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            html = res.text
            
            # 1. استخراج الـ User ID
            uid_match = re.search(r'\"userId\":\"(\d+)\"', html)
            uid = uid_match.group(1) if uid_match else "N/A"
            
            # 2. استخراج الدولة/المنطقة
            region_match = re.search(r'\"region\":\"([A-Z]{2})\"', html)
            region = region_match.group(1) if region_match else "N/A"
            
            # 3. تاريخ الإنشاء
            c_date = get_creation_date(uid) if uid != "N/A" else "N/A"
            
            # 4. صيد الإيميلات
            emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)))
            
            # 5. نوع الحساب
            verified = "verified\":true" in html
            acc_type = "Verified Official" if verified else "Standard Account"
            
            # 6. الروابط الاجتماعية
            socials = []
            for p in ['instagram', 'facebook', 'twitter', 'youtube']:
                if p in html.lower(): socials.append(p.capitalize())

            # 7. تحميل الصورة الشخصية HD
            avatar_match = re.search(r'\"avatarLarger\":\"(https://.*?)\"', html)
            if avatar_match:
                img_url = avatar_match.group(1).replace('\\u002F', '/')
                urllib.request.urlretrieve(img_url, f"{username}_avatar.jpg")
                img_status = f"Downloaded ({username}_avatar.jpg)"
            else:
                img_status = "Not Found"

            # --- عرض النتائج النهائية ---
            print(f"\n\033[1;32m[✔] Scan Finished Successfully!\033[0m")
            print(f"\033[1;37m" + "─"*45 + "\033[0m")
            print(f"\033[1;32m👤 User:\033[0m {username} | \033[1;32mType:\033[0m {acc_type}")
            print(f"\033[1;32m🆔 ID:\033[0m   {uid} | \033[1;32mRegion:\033[0m {region}")
            print(f"\033[1;32m📅 Date:\033[0m {c_date} | \033[1;32mAvatar:\033[0m {img_status}")
            print(f"\033[1;32m📧 Mail:\033[0m {', '.join(emails) if emails else 'No Public Emails'}")
            print(f"\033[1;32m🔗 Socials:\033[0m {', '.join(socials) if socials else 'None'}")
            print(f"\033[1;37m" + "─"*45 + "\033[0m")

            # حفظ التقرير
            report = {
                "dev": "AHMED",
                "target": username,
                "user_id": uid,
                "region": region,
                "created": c_date,
                "emails": emails,
                "verified": verified
            }
            with open(f"{username}_report.json", "w") as f:
                json.dump(report, f, indent=4)
            print(f"\033[1;34m[!] JSON Report Saved.\033[0m\n")

        else:
            print("\033[1;31m[-] Error: Profile not found or IP Blocked.\033[0m")
    except Exception as e:
        print(f"\033[1;31m[-] System Error: {e}\033[0m")

if __name__ == "__main__":
    banner()
    target_user = input("\033[1;37m[?] Enter Target Username: \033[0m")
    ahmed_ultimate_scan(target_user)
