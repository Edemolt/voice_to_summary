from transformers import pipeline

# Use summarization instead of feature-extraction
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """In 2023 generic drugs continued to play a critical role in the U.S. health care system allowing patients greater access to needed medicines. Generic drugs are generally lower cost than their brand-name equivalent and the approval of generic drugs often means multiple manufacturers for generic medicines, which can help stabilize the supply chain and reduce drug shortage risks.

The mission of the Office of Generic Drugs is to ensure high-quality, safe, and effective generic medicines are available to the American public. Our 2023 Annual Report provides highlights of activities and accomplishments including generic drug approvals, first generic approvals, science and research innovations for generic medicines – including complex generics, and international collaboration, as well as how we are doing on agreements made under the third iteration of the Generic Drug User Fee Amendments."""

# Get the summary
summary = summarizer(text, max_length=150, min_length=40)

# Print the summary
print(summary[0]['summary_text'])
