from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API Key
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get form data from the user
    data = request.form
    job_title = data.get('job_title')
    company_name = data.get('company_name')
    requirements = data.get('requirements')
    responsibilities = data.get('responsibilities')
    perks = data.get('perks')
    notes = data.get('notes')

    # Prompt for GPT
    prompt = f"""
    Generate a professional job description with the following details:
    - Job Title: {job_title}
    - Company Name: {company_name}
    - Must-Have Requirements: {requirements}
    - Responsibilities: {responsibilities}
    - Perks and Benefits: {perks}
    - Additional Notes: {notes}
    """

    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        job_description = response['choices'][0]['message']['content']
        return jsonify({'success': True, 'description': job_description})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)