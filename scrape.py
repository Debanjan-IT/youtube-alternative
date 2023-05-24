from youtubesearchpython import VideosSearch

def getHighestWidth(thumbnail_list):
    max = {
        'url': '',
        'width': 0,
        'height': 0
    }
    for thumbnail in thumbnail_list:
        if (thumbnail['width'] > max['width']):
            max = thumbnail
    return max['url']


def search(query):
    videosSearch = VideosSearch(query, limit = 50)
    videos = videosSearch.result()['result']
    results = []
    for video in videos:
        data = {}
        data['video_id'] = video['id']
        data['title'] = video['title']
        data['thumbnail'] = getHighestWidth(video['thumbnails'])
        data['channel'] = video['channel']['name']
        results.append(data)
        
    return results