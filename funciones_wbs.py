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

        print(v
        e)

    def parse_notice(link,today):

        try:

            if

            try:


            except
