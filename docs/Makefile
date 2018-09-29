OPEN := $(shell which open 2>/dev/null || which xdg-open 2>/dev/null)

download:
	wget https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/versions/3.0.1.md -O spec.md

push:
	shosai hatena push spec.md

see:
	${OPEN} https://pod.hatenablog.com/draft/kLzKTkeah6a8O8mYHiKDYB43dMA
