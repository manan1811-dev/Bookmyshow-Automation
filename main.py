from playwright.sync_api import sync_playwright

city = 'ahmedabad'
with sync_playwright() as p:
    browser = p.chromium.launch(
        channel="chrome",
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled",
            # "--blink-settings=imagesEnabled=false",
        ],
    )

    context = browser.new_context(
        permissions=["geolocation"],
        geolocation={"latitude": 37.7749, "longitude": -122.4194}
    )

    page = context.new_page()
    page.goto(f'https://in.bookmyshow.com/explore/home/{city}')

    page.locator("//div[contains(@class,'kudrkl')]").click()

    search = page.get_by_placeholder("Search for movies, events, plays, sports...")

    search.fill("dhabkaro")
    page.wait_for_timeout(2000)
    # page.locator("//div[contains(@class,'kOuSpD')]").click()
    
    # page.locator("//button[@data-phase='postRelease']").first.click()
    page.locator("//div[@id='generic']//div[contains(@class,'sc-1h5m8q1-0')]").first.click()
    page.locator("//button[@data-phase='postRelease']").first.click()
    main_show = page.locator("//div[contains(@class,'kJBeM')]").first
    main_show.locator("//div[contains(@class,'hlrCBW')]").last.click()
    page.locator("//button[@aria-label='Select Seats']").click()
    canvas = page.locator("canvas").nth(0)
    print(canvas.bounding_box())
    print(page.locator("canvas").count())
    print(page.locator("svg").count())
    box = canvas.bounding_box()

    canvas.click(
        position={
            "x": box["width"] / 2,
            "y": box["height"] / 2
        }
    )

    input('wait..')