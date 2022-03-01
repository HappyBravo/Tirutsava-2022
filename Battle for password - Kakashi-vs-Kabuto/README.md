<div class="span-sm-11 hr_tour-problem-statement problem-statement"><div class="content-text challenge-text mlB">
                <div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><p>You are finally inside the village, and with your help now, both of those guards are fighting Orochimaru and his army, though they won't be able to hold him for long, so you must hurry.</p>

<p>After some information gathering, you found out that the password is with Kabuto, the most trusted ally of Orochimaru. In the meantime, you also freed Kakashi (one of naruto's best friends and a strong ninja) from prison.</p>

<p>Now you and Kakashi are gonna use hypnosis Jutsu on Kabuto to find the password, but Kabuto is smart. He hid the password inside his brain in an interesting way.</p>

<p><img src="https://s3.amazonaws.com/hr-assets/0/1642433158-0beed2b821-scale_1200.png" alt="image" title=""></p>

<p>First let's define password:</p>

<ul>
<li>There is at least one digit in the string,</li>
<li>There is at least one lowercase letter of the Latin alphabet in the string,</li>
<li>There is at least one of three listed symbols in the string: '#', '*', '&amp;'.</li>
</ul>

<p>Inside his brain you saw a screen which had n number of strings each of size m.</p>

<p>For each character of the password we have a fixed string of length m, on each of these n strings there is a pointer on some character. The i-th character displayed on the screen is the pointed character in the i-th string. Initially, all pointers are on characters with indexes 1 in the corresponding strings (all positions are numbered starting from one).</p>

<p>During one operation Kakashi can move a pointer in one string one character to the left or to the right. Strings are cyclic, it means that when we move the pointer which is on the character with index 1 to the left, it moves to the character with the index m, and when we move it to the right from the position m it moves to the position 1.</p>

<p>You need to determine the minimum number of operations necessary to make the string displayed on the screen a valid password.</p>

<p>You have such input data that you can always get a valid password.</p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><p>The first line contains two integers n, m — the length of the password and the length of strings which are assigned to password symbols.</p>

<p>Each of the next n lines contains the string which is assigned to the i-th symbol of the password string. Its length is m, it consists of digits, lowercase English letters, and characters '#', '*' or '&amp;'.</p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><ul>
<li>3 ≤ n ≤ 50</li>
<li>1 ≤ m ≤ 50</li>
</ul></div></div></div><div class="challenge_output_format"><div class="msB challenge_output_format_title"><p><strong>Output Format</strong></p></div><div class="msB challenge_output_format_body"><div class="hackdown-content"><p>Print one integer — the minimum number of operations which is necessary to make the string, which is displayed on the screen, a valid password.</p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 0</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><div class="highlight"><pre><span></span><span class="err">3 4</span>
<span class="err">1**2</span>
<span class="err">a3*0</span>
<span class="err">c4**</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 0</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><div class="highlight"><pre><span class="err">1</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 0</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><p>it is necessary to move the pointer of the third string to one left to get the optimal answer.</p>

<p><img src="https://s3.amazonaws.com/hr-assets/0/1642433854-9a4650594d-d650689efbf9a32a4d6f144e467f288e939baa4a.png" alt="image" title=""></p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 1</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><div class="highlight"><pre><span></span><span class="err">5 5</span>
<span class="err">#*&amp;#*</span>
<span class="err">*a1c&amp;</span>
<span class="err">&amp;q2w*</span>
<span class="err">#a3c#</span>
<span class="err">*&amp;#*&amp;</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 1</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><div class="highlight"><pre><span class="err">3</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 1</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><p>one of possible algorithms will be:</p>

<ul>
<li>to move the pointer of the second symbol once to the right.</li>
<li>to move the pointer of the third symbol twice to the right.</li>
</ul>

<p><img src="https://s3.amazonaws.com/hr-assets/0/1642433934-4d666cd1b7-0daf99969920d860c68914d9342b056ac4462413.png" alt="image" title=""></p></div></div></div>
            </div></div>
