# My FastAPI Tutorial
- use REST Client to test API endpoints `rest_client.http`

## Sources
- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [best tutorial @Perplexity](./docs/best_tutorial_PERPLEXITY.md)
- [how to learn FastAPI @ChatGPT](./docs/how_to_learn_FASTAPI_CHATGPT.md)
- [how to learn FastAPI @Gemini](./docs/how_to_learn_FASTAPI_GEMINI.md)

## ANKI files
- [anki dir](./anki/)

## Recap

### First Step
- [src/a001_first_step/main.py](./src/a001_first_step/main.py)
- app is a FastAPI instance that subclasses from Starlette (!!!)
- the way `typing.Annotated` is used (!!!)

### Path Parameters
- you can declare path parameters/variables in the path string by using curly braces: `/items/{item_id}`
- path parameter will be passed as function arguments -> *if argument has a different name than the parameter in the path string it will be treated as a query parameter* check next section.
- when you annotate path parameters with types, FastAPI will perform data validation and conversion automatically (!!!) this is super useful mind that validation + conversion.
    - can use `Enum` calls for limiting possible values -> will also be reflected in OpenAPI schema + docs (!!!)
- based on the type annotation, FastAPI will generate OpenAPI schema automatically + docs (!!!)
- under the hood uses Pydantic for data validation and conversion (!!!)
- order of path registration matters, evaluated in order of declaration
- path parameters containing paths (???) what is the use case?

### Query Parameters
- query parameters are not declared in the path string, but as function parameters with default values
- TAKEAWAY: handle response as dict and update accordingly to query parameters
<!-- cSpell:disable-next-line -->
- QQQ: pojawia się pytanie skoro "type annotation" argumentów funkcji jest odzwierciedlone w dokumentcji OpenAPI to czy można w ten sam sposób okrślich "Schema" dla return type funkcji endpointu? -> TAK można użyć `response_model`

## What is this?
<!-- cSpell:words fastapi -->
- `fastapi-cloud-cli`
- OpenAPI schema