<
# este es el mater





def parse_notice(link,today):

    try:
        response= requests.get(link)
        if response.status_code==200:
            notice=response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title=parsed.xpath(XPATH_TITLE)[0]
                title=title.replace('\"',(''))
                sumary= parsed.xpath(XPATH_SUMARY)[0]
                body=parsed.xpath(XPATH_BODY)
            except IndexError:
                print ("e")
                return

            with open(f'{today}/{title}.txt','w',encoding = 'utf-8')as f:
                f.write(title)
                f.write('\n\n')
                f.write(sumary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'error:{response.status_code}')

    except  ValueError as ve:

        print(ve)
# cabecera   union
def parse_home():
    try:
        response= requests.get(HOME_URL)
        if response.status_code ==200:
           home=response.content.decode('utf-8')
           parsed=html.fromstring(home)
           links_to_notices=parsed.xpath(XPATH_Link_TO_ARTICLE)
           #print(links_to_notices)
           today= datetime.date.today().strftime('%d-%m-%Y')
           if not os.path.isdir(today):
                os.mkdir(today)

           for link in links_to_notices:
                parse_notice(link, today)
        else:
            raise valueError(f'error:{response.status_code}')
    except ValueError as ve:
        print(ve)
