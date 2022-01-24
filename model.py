from pydantic import BaseModel


class Release(BaseModel):
    Protocol: str
    name: str
    tag_name: str
    published_at: str
    url: str
    date_ago: str
    body: str = None
