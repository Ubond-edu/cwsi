# Import necessary libraries
import streamlit as st
import openai

# Define main function for the streamlit app
def main():

    st.title("CWSI Argument Feedback")
    
    # Create a text input box for the writing sample
    user_input = st.text_area("Enter your text here:", height=200)

    # Access the OpenAI API Key from secrets
    openai_api_key = st.secrets["openai_api_key"]

    # Set the OpenAI API key
    openai.api_key = openai_api_key
    
    # Create a button that when clicked will generate feedback
    if st.button("Get Feedback"):
        # Use OpenAI's API to generate feedback
        model = "text-davinci-003"
        prompt = f"""
You are this ESL young learner's debate teacher. Write a constructive, supportive and honest feedback report to the learner about their performance on the CWSI argument model writing task.
A CWSI model argument has the following format:
1. Claim - the thesis or main point of the argument. e.g. "Soda drinks should be banned" (this needn't include a reason)
2. Warrant - the reasoning that supports the claim. e.g. "Because, soda drinks are unhealthy"
3. Support - the evidence and/or examples that support the claim. e.g. "For example, the NCBI found that soda contains a lot of sugar which is a known cause of diabetes"
4. Impact - the consequence (why the audience should care). e.g. "This is important because diabetes kills more than 50,000 people per year and substantially reduces quality of life."

Part 1: Friendly and supportive opening
For example, a student who did very well might get a statement like: "Great job! You're doing really well at writing CWSI arguments.". Whereas, a 
student who has significant problems might get a statement like: "Great effort! There's some parts of your CWSI argument that are really good and some parts that could use improvement."

Part 2: Use the following rubric to analyze the student writing (comment on every category):
"1. Is the claim/thesis is a clear statement that can be supported with evidence and facts?
2. Is the warrant/reasoning for the claim clear and logical? Is connective language like 'because' used?
3. Are clear and persuasive evidence or examples are provided that logically support the warrant and claim?
4. Is the impact/consequence of the claim clear and substantial? Ideally, is the impact is quantified?
5. Overall, is the CWSI argument in its entirety written persuasively?
6. Were there any errors in English usage that need correcting?"

Part 3: Provide some suggestions on how to elaborate their argument to make it more persuasive. For example, you could suggest adding additional examples, 
suggest quantifying an impact, using more descriptive or persuasive language, etc. You could also provide modeling for the learner if the have missed a 
part of the argument. If you give a suggestion, try to give them an example of how to do it. 

Finally:
Check your report for consistency, accuracy, and completeness of the steps above. Remember, you are the teacher and you are writing to the student.
Here's the student writing to evaluate:
{user_input}

"""

        try:
            response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=500, temperature=0.3)
            feedback = response.choices[0].text.strip()
        except Exception as e:
            st.error(f"Error: {e}")
            return None

        # Display the feedback in a new text box
        st.text_area("Feedback:", value=feedback, height=400)

# Call the main function
if __name__ == "__main__":
    main()
