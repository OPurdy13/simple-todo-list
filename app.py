<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple To-Do List</title>
  <meta name="description" content="A clean, simple, and free-to-use To-Do List web app with no login required.">
  <meta name="keywords" content="To-Do List, Simple Task Manager, No Login, Free Task App">
  <meta name="author" content="Your Name">
  <link rel="icon" href="assets/favicon.ico" type="image/x-icon">
  <link rel="stylesheet" href="style/main.css">
  <style>
    body {
      background: #f9fafb;
      font-family: sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .container {
      background: #fff;
      padding: 2rem;
      border-radius: 1rem;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      width: 90%;
      max-width: 400px;
    }

    h1 {
      text-align: center;
      margin-bottom: 1rem;
      color: #111827;
    }

    .input-group {
      display: flex;
      gap: 0.5rem;
    }

    #task-input {
      flex: 1;
      padding: 0.5rem;
      border: 1px solid #d1d5db;
      border-radius: 0.5rem;
    }

    #add-btn {
      padding: 0.5rem 1rem;
      background: #3b82f6;
      color: white;
      border: none;
      border-radius: 0.5rem;
      cursor: pointer;
    }

    #task-list {
      list-style: none;
      padding: 0;
      margin-top: 1rem;
    }

    #task-list li {
      display: flex;
      justify-content: space-between;
      padding: 0.5rem;
      background: #f3f4f6;
      margin-bottom: 0.5rem;
      border-radius: 0.5rem;
    }

    #task-list li.completed {
      text-decoration: line-through;
      color: #9ca3af;
    }

    .controls {
      display: flex;
      justify-content: space-between;
      margin-top: 1rem;
    }

    .controls button {
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 0.5rem;
      cursor: pointer;
      background: #e5e7eb;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>📝 My To-Do List</h1>
    <div class="input-group">
      <input type="text" id="task-input" placeholder="Add a new task...">
      <button id="add-btn">Add</button>
    </div>
    <ul id="task-list"></ul>
    <div class="controls">
      <button id="clear-completed">Clear Completed</button>
      <button id="mark-all">Mark All Done</button>
    </div>
  </div>

  <script>
    const taskInput = document.getElementById('task-input');
    const addBtn = document.getElementById('add-btn');
    const taskList = document.getElementById('task-list');
    const clearCompleted = document.getElementById('clear-completed');
    const markAll = document.getElementById('mark-all');

    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    function saveTasks() {
      localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    function renderTasks() {
      taskList.innerHTML = '';
      tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';

        const span = document.createElement('span');
        span.textContent = task.text;
        span.addEventListener('click', () => toggleTask(index));

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = '❌';
        deleteBtn.addEventListener('click', () => deleteTask(index));

        li.appendChild(span);
        li.appendChild(deleteBtn);
        taskList.appendChild(li);
      });
    }

    function addTask() {
      const text = taskInput.value.trim();
      if (text !== '') {
        tasks.push({ text, completed: false });
        taskInput.value = '';
        saveTasks();
        renderTasks();
      }
    }

    function toggleTask(index) {
      tasks[index].completed = !tasks[index].completed;
      saveTasks();
      renderTasks();
    }

    function deleteTask(index) {
      tasks.splice(index, 1);
      saveTasks();
      renderTasks();
    }

    clearCompleted.addEventListener('click', () => {
      tasks = tasks.filter(task => !task.completed);
      saveTasks();
      renderTasks();
    });

    markAll.addEventListener('click', () => {
      tasks.forEach(task => task.completed = true);
      saveTasks();
      renderTasks();
    });

    addBtn.addEventListener('click', addTask);
    taskInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') addTask();
    });

    renderTasks();
  </script>
</body>
</html>
