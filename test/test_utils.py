import pytest

from utils import check_flag


@pytest.mark.asyncio
async def test_get_post_exists():
    msg = "hardfork asl;kdjfifnvrtughasdochjcrgg"
    assert await check_flag(msg) == [":pushpin: Here's hardfork in body.", ":pushpin: Here's fork in body."]

