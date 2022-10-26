def link_serializer(link) -> dict:
    return {
        "id": str(link["_id"]),
        "name": link['name'],
        "link": link['link'],
        "type": link['type'],
        "tags": link['tags'],
    }

def links_serializer(links) -> list:
    return [link_serializer(link) for link in links]