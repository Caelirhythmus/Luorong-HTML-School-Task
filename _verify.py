import re

pages = {
    'index.html': ['about.html', 'hobbies.html'],
    'about.html': ['index.html', 'hobbies.html'],
    'hobbies.html': ['index.html', 'about.html'],
}

all_ok = True
for page, expected_links in pages.items():
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    has_doctype = '<!DOCTYPE html>' in content
    has_html = '</html>' in content
    has_title = '<title>' in content
    has_profile = 'profile-photo.jpg' in content

    links_found = re.findall(r'href="([^"]+)"', content)
    page_ok = True
    for link in expected_links:
        if link not in links_found:
            print(f'  MISSING link: {page} -> {link}')
            page_ok = False
            all_ok = False

    nav_match = re.search(r'<nav.*?</nav>', content, re.DOTALL)
    has_self_active = False
    if nav_match:
        nav_content = nav_match.group()
        if f'href="{page}"' in nav_content and 'active' in nav_content:
            has_self_active = True

    print(f'{page}:')
    print(f'  doctype={has_doctype}, html={has_html}, title={has_title}, profile_img={has_profile}')
    print(f'  self_active={has_self_active}, links_ok={page_ok}')
    print()

if all_ok:
    print('All pages verified successfully.')
