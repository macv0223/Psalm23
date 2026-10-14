"""Local layout smoke check using Playwright set_content (works without HTTP access)."""
from pathlib import Path
import base64,re
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
page_html=(root/'dist/index.html').read_text()
css=(root/'dist/assets/site.css').read_text()
css=re.sub(r'@import[^;]+;','',css,count=1)
js=(root/'dist/assets/app.js').read_text()
for f in ['favicon.svg','hauling-scene.svg','brand-mark.svg']:
 uri='data:image/svg+xml;base64,'+base64.b64encode((root/'dist/assets'/f).read_bytes()).decode()
 page_html=page_html.replace('assets/'+f,uri)
logo_fallback='data:image/svg+xml;base64,'+base64.b64encode((root/'dist/assets/brand-mark.svg').read_bytes()).decode()
page_html=page_html.replace('https://psalm-23-transportation.igarza5652.chatgpt.site/logo.jpeg',logo_fallback)
page_html=page_html.replace('<link rel="stylesheet" href="assets/site.css">','<style>'+css+'</style>')
page_html=page_html.replace('<script type="module" src="assets/app.js"></script>','<script>'+js+'</script>')
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 for name,w,h in [('desktop',1440,960),('mobile',390,844)]:
  page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
  problems=[]
  page.on('pageerror',lambda e:problems.append(str(e)))
  page.set_content(page_html,wait_until='domcontentloaded')
  page.wait_for_timeout(200)
  assert page.locator('h1').inner_text().replace('\n',' ').startswith('Anything.')
  assert page.locator('.service-card').count()==3
  assert page.locator('#quote-form input').count()==4
  if name=='mobile':
   toggle=page.locator('.menu-toggle');toggle.click()
   assert toggle.get_attribute('aria-expanded')=='true'
   assert page.locator('#primary-navigation').is_visible()
   page.locator('#primary-navigation a[href="#services"]').click()
   assert toggle.get_attribute('aria-expanded')=='false'
  page.screenshot(path=str(root.parent/f'psalm-23-preview-{name}.png'),full_page=True,animations='disabled')
  width=page.locator('body').evaluate('(e) => [e.scrollWidth,e.clientWidth]')
  print(name,'page title:',page.title(),'body scroll/client widths:',width,'JavaScript exceptions:',problems)
  assert width[0] <= w+2, 'Page overflows horizontally'
  assert problems==[]
  page.close()
 browser.close()
