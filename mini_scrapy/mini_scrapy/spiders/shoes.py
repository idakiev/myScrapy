import scrapy


class ShoesSpider(scrapy.Spider):
    name = "shoes"
    start_urls = ["https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes"]

    def parse(self, response, **kwargs):
        name_section = response.css('[data-auid="PDP_ProductName"]')
        price_section = response.css('.nowPrice')
        rating_section = response.css('span.ratingAvg')
        reviews_section = response.css('button.ratingCount')
        default_colour_section = response.css('[data-auid="PDP-title"] div:last-child > span span:last-child')
        colors_section = response.css('div#swatch-drawer-content button')

        colours_list = []
        for colour in colors_section:
            colours_list.append(colour.attrib['aria-label'])

        yield {
            'name': name_section.css('::text').extract(),
            'price': price_section.css('::text').extract(),
            'colour': default_colour_section.css('::text').extract(),
            'reviews_count': reviews_section.css('::text').extract(),
            'reviews_score': rating_section.css('::text').extract(),
            'availableColours': colours_list,
        }
