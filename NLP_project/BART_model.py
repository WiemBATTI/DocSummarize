from transformers import BartTokenizer, BartForConditionalGeneration
import torch



model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)



def divide_text_into_segments(text, max_length):

    tokens = tokenizer.tokenize(text)
    segments = []
    current_position = 0

    while current_position < len(tokens):
        # Find the end of the segment at a logical point
        end_position = current_position + max_length
        while end_position < len(tokens) and tokens[end_position] not in ['.',',']:
            end_position -= 1
        
        # Add the segment to the list
        segments.append(tokenizer.convert_tokens_to_string(tokens[current_position:end_position+1]).strip())
        
        # Move to the next segment
        current_position = end_position + 1
    
    return segments



def generate_summary(text):
    max_length = model.config.max_position_embeddings - 2  # Account for special tokens
    text_segments=divide_text_into_segments(text, max_length)
    
    #Test pour minimiser le nombre de fois de l'execution du modele
    if (len(text_segments)>=5) and (len(text_segments)<=15):
        pas=2
    elif len(text_segments)>15:
        pas=3
    else:
        pas=1
    summaries = []

    for i in range(0,len(text_segments),pas):
        segment=text_segments[i]
        inputs = tokenizer.encode("summarize: " + segment, return_tensors="pt", max_length=max_length, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=50,  early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)


    full_summary = " ".join(summaries)
    return full_summary
    



