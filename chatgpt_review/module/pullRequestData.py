class PullRequestData:
    def __init__(self):
        self.author = None
        self.create_time = None
        self.title = None
        self.body = None
        self.url = None
        self.number = None
        self.comments = []

    # def __init__(self, author,body,review_author,mention,url,create_time,path):
    #     self.writeAuthor = author
    #     self.reviewAuthor = review_author
    #     self.body = body
    #     self.mention = mention
    #     self.url = url
    #     self.create_time = create_time
    #     self.path = path

    def print(self):
        print("  ", "Title:", self.title)
        print("  ","Author:",self.author)
        # print("  ", "Body:", self.body)
        print("  ", "url:", self.url)
        print("  ", "create_time:", self.create_time)
        print("  ", "number:", self.number)
        print("  ", "Comments:", len(self.comments))


class Comment:
    def __init__(self):
        self.pr_url = None
        self.url = None
        self.comment_text = None
        self.author = None
        self.has_chatGPT_link = False



