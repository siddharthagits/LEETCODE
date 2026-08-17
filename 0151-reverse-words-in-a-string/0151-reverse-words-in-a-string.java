class Solution {
    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        Deque<String> st = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == ' ') {
                if (!sb.toString().equals("")) {
                    st.push(sb.toString());
                }
                sb.setLength(0);
                continue;
            }

            sb.append(ch);
        }

        if (sb.length() != 0) {
            st.push(sb.toString());
            sb.setLength(0);
        }

        while (!st.isEmpty()) {
            sb.append(st.pop());
            if (!st.isEmpty())
                sb.append(" ");
        }

        return sb.toString();
    }
}