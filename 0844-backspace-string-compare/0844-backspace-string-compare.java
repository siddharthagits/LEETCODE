class Solution {
    public boolean backspaceCompare(String s, String t) {
        return build(s).equals(build(t));
    }

    private String build(String str) {
        StringBuilder sb = new StringBuilder();   // acts as our stack
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch != '#') {
                sb.append(ch);                   // regular char -> keep
            } else if (sb.length() > 0) {
                sb.deleteCharAt(sb.length() - 1); // backspace -> erase last
            }
        }
        return sb.toString();
    }
}