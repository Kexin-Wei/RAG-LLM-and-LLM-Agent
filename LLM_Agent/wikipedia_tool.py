import wikipedia


class WikipediaTools:
    @staticmethod
    def get_functions_with_descriptions():
        return [
            {
                "name": "search_wikipedia_pages",
                "description": "Search for Wikipedia pages based on a query.",
                "example": {"query": "Artificial Intelligence"},
            },
            {
                "name": "get_wikipedia_page_summary",
                "description": "Get a summary of a Wikipedia page.",
                "example": {"title": "Artificial Intelligence", "sentences": 3},
            },
            {
                "name": "get_wikipedia_page_content",
                "description": "Get the content of a Wikipedia page.",
                "example": {"title": "Artificial Intelligence"},
            },
        ]

    @staticmethod
    def get_function_names():
        return [
            func["name"] for func in WikipediaTools.get_functions_with_descriptions()
        ]

    @staticmethod
    def search_wikipedia_pages(query):
        return wikipedia.search(query)

    @staticmethod
    def get_wikipedia_page_summary(title, sentences):
        return wikipedia.summary(title, sentences=sentences)

    @staticmethod
    def get_wikipedia_page_content(title):
        return wikipedia.page(title).content
