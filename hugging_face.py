import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

from langchain import PromptTemplate, HuggingFaceHub, LLMChain
# initialize HF LLM
flan_t5 = HuggingFaceHub(
    repo_id="google/flan-t5-xxl",
    model_kwargs={"temperature":1}
)

# The LLM takes a prompt as an input and outputs a completion
template = "What are the important places when we drive from London to Paris ? "

completion = flan_t5(template)

print(completion)
# prompt = PromptTemplate(template=template, input_variables=["animal"])

# llm_chain = LLMChain(
#    prompt=prompt,
#     llm=flan_t5
#  )

# print(llm_chain.run())

# # build prompt template for simple question-answering
# template = """Question: {question}

# Answer: """
# prompt = PromptTemplate(template=template, input_variables=["question"])

# llm_chain = LLMChain(
#     prompt=prompt,
#     llm=flan_t5
# )


# qs = [
#     {'question': "Which NFL team won the Super Bowl in the 2010 season?"},
#     {'question': "If I am 6 ft 4 inches, how tall am I in centimeters?"},
#     {'question': "Who was the 12th person on the moon?"},
#     {'question': "How many eyes does a blade of grass have?"}
# ]
# res = llm_chain.generate(qs)
# print(res)

# multi_template = """Answer the following questions one at a time.

# Questions:
# {questions}

# Answers:
# """
# long_prompt = PromptTemplate(
#     template=multi_template,
#     input_variables=["questions"]
# )

# llm_chain = LLMChain(
#     prompt=long_prompt,
#     llm=flan_t5
# )

# qs_str = (
#     "Which NFL team won the Super Bowl in the 2010 season?\n" +
#     "If I am 6 ft 4 inches, how tall am I in centimeters?\n" +
#     "Who was the 12th person on the moon?" +
#     "How many eyes does a blade of grass have?"
# )

# print(llm_chain.run(qs_str))