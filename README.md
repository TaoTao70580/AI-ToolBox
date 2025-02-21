When it comes to tax season, it can be very stressful, especially for taxpayers who are not in the accounting field or are not native English speakers. In recent years, significant breakthroughs in artificial intelligence (AI) and machine learning (ML) are expected to transform various aspects of daily life. In particular, large language models (LLMs) have been used across numerous domains.
In this repo, we leverage AI models to assist the general public, including individuals with diverse language backgrounds, in understanding the latest IRS news. Specifically, we employ the Llama-2-7b-chat-hf model, an open-source large language model developed by Meta (https://llama.meta.com), to automatically generate summaries and Q&A (question-and-answer) pairs from tax-related news. Additionally, we use the AI model to detect and verify potential fake tax news.
We also explore the use of a machine learning model, Scikit-learn, to predict future tax trends based on previous years' data.

Python code is developed for this purpose. The Python code is developed in a Linux RedHat environment.

- Data preprocess: parse.py
- Generate Q&A pairs : q_and_a.py
- Generate summary: summary.py
- Translate into other languages: translate.py
- Converts text output into MP3 : voice.py
- Detect misinformation in the input : check_fake_info.py
- Predict future tax : future_tax.py
- Cauculate tax: cauculate_tax.py
