class Article:
    '''
    Articles class to define News Objects
    '''
    def __init__(self,id,author,title,description,url,image_url,content,publishedAt,source_name,source_id):
        self.id =id
        self.title = title
        self.description= description
        self.url = url
        self.image_url = image_url
        self.publishedAt
        self.author
        self.source_name = source_name
        self.source_id = source_id
        # self.vote_count = vote_count