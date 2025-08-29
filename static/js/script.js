// Function to process array through the API
async function processArray() {
    const input = document.getElementById('arrayInput').value.trim();
    const output = document.getElementById('responseOutput');
    
    if (!input) {
        output.innerHTML = '<span class="error">Please enter some data to process.</span>';
        return;
    }
    
    // Show loading state
    output.innerHTML = '<span class="loading">Processing...</span>';
    
    try {
        // Parse input string to array
        const data = input.split(',').map(item => item.trim()).filter(item => item !== '');
        
        // Prepare request payload
        const payload = {
            data: data
        };
        
        // Make API call
        const response = await fetch('/bfhl', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
        });
        
        const result = await response.json();
        
        // Display result
        if (result.is_success) {
            output.innerHTML = `<span class="success">✅ Request successful!</span>\n\n${JSON.stringify(result, null, 2)}`;
        } else {
            output.innerHTML = `<span class="error">❌ Error: ${result.error || 'Unknown error'}</span>\n\n${JSON.stringify(result, null, 2)}`;
        }
        
    } catch (error) {
        output.innerHTML = `<span class="error">❌ Network error: ${error.message}</span>`;
    }
}

// Function to load example data
function loadExample(exampleData) {
    document.getElementById('arrayInput').value = exampleData;
}

// Function to handle Enter key press
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        processArray();
    }
}

// Add event listeners when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Add keypress listener to input field
    document.getElementById('arrayInput').addEventListener('keypress', handleKeyPress);
    
    // Add click listener to process button (as backup)
    document.querySelector('.btn-primary').addEventListener('click', processArray);
    
    // Add click listeners to example buttons
    document.querySelectorAll('.btn-example').forEach(button => {
        button.addEventListener('click', function() {
            const exampleData = this.textContent.replace('Example ', '').toLowerCase();
            let data;
            
            switch(exampleData) {
                case 'a':
                    data = 'a,1,334,4,R,$';
                    break;
                case 'b':
                    data = '2,a,y,4,&,-,*,5,92,b';
                    break;
                case 'c':
                    data = 'A,ABcD,DOE';
                    break;
                default:
                    data = 'a,1,334,4,R,$';
            }
            
            loadExample(data);
        });
    });
});

// Function to copy response to clipboard
function copyToClipboard() {
    const output = document.getElementById('responseOutput');
    const text = output.textContent;
    
    navigator.clipboard.writeText(text).then(function() {
        // Show temporary success message
        const originalContent = output.innerHTML;
        output.innerHTML = '<span class="success">✅ Copied to clipboard!</span>';
        
        setTimeout(() => {
            output.innerHTML = originalContent;
        }, 2000);
    }).catch(function(err) {
        console.error('Could not copy text: ', err);
    });
}

// Add keyboard shortcuts
document.addEventListener('keydown', function(event) {
    // Ctrl/Cmd + Enter to process array
    if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
        event.preventDefault();
        processArray();
    }
    
    // Ctrl/Cmd + C to copy response
    if ((event.ctrlKey || event.metaKey) && event.key === 'c') {
        const activeElement = document.activeElement;
        if (activeElement.id === 'responseOutput') {
            copyToClipboard();
        }
    }
});
